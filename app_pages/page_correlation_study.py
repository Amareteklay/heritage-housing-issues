import streamlit as st
from src.data_management import load_housing_data
import matplotlib.pyplot as plt
import seaborn as sns
import ppscore as pps
sns.set_style("whitegrid")
from feature_engine.discretisation import ArbitraryDiscretiser
import numpy as np
import plotly.express as px

def page_correlation_study_body():
    """
    Display correlated features and a checkbox to show the show
    house price per variable.
    """
    df = load_housing_data()

    vars_to_study = ['1stFlrSF', 'GarageArea', 'GrLivArea', 'KitchenQual', 'MasVnrArea', 'OpenPorchSF', 'OverallQual', 'TotalBsmtSF', 'YearBuilt', 'YearRemodAdd']

    st.write("### Housing Prices Correlation Study")
    st.info(
        f"* The client is interested in identifying the features that have strong correlation with "
        f"house prices so that she can maximize the sales revenue."
    )

    # inspect data
    if st.checkbox("Inspect Housing Data"):
        st.write(
            f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns, "
            f"find below the first 10 rows.")
        
        st.write(df.head(10))

    st.write("---")


    # Correlation Study Summary
    st.write(
        f"* A correlation study was conducted in the notebook to better understand how "
        f"the variables are correlated to Churn levels. \n"
        f"The most correlated variable are: **{vars_to_study}**"
    )


    # Text based on "03 - Correlation_Study" notebook - "Conclusions and Next steps" section
    st.info(
        f"We make the following observations from both the correlation analysis and the plots.\n"
        f"* Higher values of 1stFlrSF, garage area, GrLivArea, MasVnrArea and TotalBsmtSF are associated with higher sale price.\n"
        f"* Houses with recently built garages or recently added remods have higher prices than those of earlier ones.\n"  
        f"* Higher Overall quality indicates higher sale prices but kitchen quality does not show clear pattern.\n" 
    )


    df_eda = df.filter(vars_to_study + ['SalePrice'])


    # Individual plots per variable
    if st.checkbox("House Prices per Variable"):
        house_price_per_variable(df_eda)
    

    if st.checkbox("Heatmaps: Pearson, Spearman and PPS Correlations"):
        df_corr_pearson, df_corr_spearman, pps_matrix = CalculateCorrAndPPS(df)
        DisplayCorrAndPPS(df_corr_pearson = df_corr_pearson,
                  df_corr_spearman = df_corr_spearman, 
                  pps_matrix = pps_matrix,
                  CorrThreshold = 0.4, PPS_Threshold =0.2,
                  figsize=(12,10), font_annot=10)


def house_price_per_variable(df_eda):
    """
    Generate box plot, line plot or scatter plot of SalePrice and
    the house features 
    """
    vars_to_study = ['1stFlrSF', 'GarageArea', 'GrLivArea', 'KitchenQual', 'MasVnrArea', 'OpenPorchSF', 'OverallQual', 'TotalBsmtSF', 'YearBuilt', 'YearRemodAdd']
    time = ['YearBuilt', 'YearRemodAdd']
    target_var = 'SalePrice'
    
    for col in vars_to_study:
        if len(df_eda[col].unique()) <= 10:
            plot_box(df_eda, col, target_var)
            print("\n\n")
        else:
            if col in time:
                plot_line(df_eda, col, target_var)
                print("\n\n")
            else:
                plot_lm(df_eda, col, target_var)
                print("\n\n")



def plot_lm(df, col, target_var):
    """
    Generate scatter plot
    """
    fig, axes = plt.subplots(figsize=(12, 6))
    sns.regplot(data=df, x=col, y=target_var, ci=None)
    plt.title(f"{col}", fontsize=20)        
    st.pyplot(fig) # st.pyplot() renders image, in notebook is plt.show()

def plot_line(df, col, target_var):
    """
    Generate line plot
    """
    fig, axes = plt.subplots(figsize=(12, 6))
    sns.lineplot(data=df, x=col, y=target_var)
    plt.title(f"{col}", fontsize=20)        
    st.pyplot(fig) # st.pyplot() renders image, in notebook is plt.show()

def plot_box(df, col, target_var):
    """
    Generate box plot
    """
    fig, axes = plt.subplots(figsize=(12, 6))
    sns.boxplot(data=df, x=col, y=target_var) 
    plt.title(f"{col}", fontsize=20)
    st.pyplot(fig) # st.pyplot() renders image, in notebook is plt.show()

## Heatmaps

def heatmap_corr(df,threshold, figsize=(20,12), font_annot = 8):
  """
  Function to create heatmap using correlations.
  """
  if len(df.columns) > 1:
    mask = np.zeros_like(df, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True
    mask[abs(df) < threshold] = True

    fig, axes = plt.subplots(figsize=figsize)
    sns.heatmap(df, annot=True, xticklabels=True, yticklabels=True,
                mask=mask, cmap='viridis', annot_kws={"size": font_annot}, ax=axes,
                linewidth=0.5
                     )
    axes.set_yticklabels(df.columns, rotation = 0)
    plt.ylim(len(df.columns),0)
    st.pyplot(fig)


def heatmap_pps(df,threshold, figsize=(20,12), font_annot = 8):
    """
    Function to create heatmap using pps.
    """
    if len(df.columns) > 1:

      mask = np.zeros_like(df, dtype=np.bool)
      mask[abs(df) < threshold] = True

      fig, ax = plt.subplots(figsize=figsize)
      ax = sns.heatmap(df, annot=True, xticklabels=True,yticklabels=True,
                       mask=mask,cmap='rocket_r', annot_kws={"size": font_annot},
                       linewidth=0.05,linecolor='grey')
      
      plt.ylim(len(df.columns),0)
      st.pyplot(fig)


def CalculateCorrAndPPS(df):
  """
  Function to calculate correlations and pps.
  """
  df_corr_spearman = df.corr(method="spearman")
  df_corr_spearman.name = 'corr_spearman'
  df_corr_pearson = df.corr(method="pearson")
  df_corr_pearson.name = 'corr_pearson'

  pps_matrix_raw = pps.matrix(df)
  pps_matrix = pps_matrix_raw.filter(['x', 'y', 'ppscore']).pivot(columns='x', index='y', values='ppscore')

  pps_score_stats = pps_matrix_raw.query("ppscore < 1").filter(['ppscore']).describe().T
  print(pps_score_stats.round(3))

  return df_corr_pearson, df_corr_spearman, pps_matrix


def DisplayCorrAndPPS(df_corr_pearson, df_corr_spearman, pps_matrix,CorrThreshold,PPS_Threshold,
                      figsize=(20,12), font_annot=8 ):
  """
  Function to display the correlations and pps.
  """

  heatmap_corr(df=df_corr_spearman, threshold=CorrThreshold, figsize=figsize, font_annot=font_annot)

  heatmap_corr(df=df_corr_pearson, threshold=CorrThreshold, figsize=figsize, font_annot=font_annot)

  heatmap_pps(df=pps_matrix,threshold=PPS_Threshold, figsize=figsize, font_annot=font_annot)