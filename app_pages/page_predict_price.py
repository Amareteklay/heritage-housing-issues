import streamlit as st
import pandas as pd
from src.data_management import load_housing_data, load_heritage_data, load_pkl_file
from src.machine_learning.predictive_analysis_ui import predict_price, predict_inherited_house_price 

def page_predict_price_body():
	
	# load predict price files
	version = 'v2'
	regression_pipe = load_pkl_file(f"outputs/ml_pipeline/predict_price/{version}/regression_pipeline.pkl")
	house_features = (pd.read_csv(f"outputs/ml_pipeline/predict_price/{version}/X_train.csv")
					.columns
					.to_list()
					)


	st.write("### Predicting sales price of inherited houses")
	st.info(
       f"* The client is interested in predicting the house sale prices from her 4 inherited houses,"
       f" and any other house in Ames, Iowa."
	)

	# Predict sales prices of inherited houses

	st.write(f"###### Predicted sales price of inherited houses")

	X_inherited = load_heritage_data()
	summed_price = 0
	predicted_sale_price = []
	for i in range(X_inherited.shape[0]):
		pprice = predict_inherited_house_price(X_inherited.iloc[[i,]], house_features, regression_pipe)
		predicted_sale_price.append(round(pprice))
		summed_price = summed_price + pprice
		summed_price = round(summed_price)
	X_inherited = X_inherited.filter(house_features)
	X_inherited['PredictedSalePrice'] = predicted_sale_price
	st.write(X_inherited.head())
	st.write(f"* Summed price: **{summed_price}** \n"
	         f"* Features used: **{X_inherited.columns.to_list()}**."
			 )
	
	st.write("---")
	# Generate Live Data
	# check_variables_for_UI(price_features)
	st.write("### House Price Predictor Interface")
	
	st.write("#### Do you want to predict sale price of another house?")
	st.write("Provide the correct values of the following attributes and click on the 'Predict Sale Price' button.")
	
	X_live = DrawInputsWidgets()


	# predict on live data
	if st.button("Predict Sale Price"): 
		price_prediction = predict_price(X_live, house_features, regression_pipe)
		
		if price_prediction == 1:
			predict_price(X_live, house_features, regression_pipe)
			



def check_variables_for_UI(house_features):
	st.write(f"* There are {len(house_features)} features for the UI: \n\n {house_features}")



def DrawInputsWidgets():

	# load dataset
	df = load_housing_data()
	
	percentageMin, percentageMax = 0.4, 2.0

    # we create input widgets only for 6 features	
	col1, col2, col3, col4 = st.columns(4)
	col5, col6, col7, col8 = st.columns(4)

	# We are using these features to feed the ML pipeline - values copied from check_variables_for_UI() result
		

	# create an empty DataFrame, which will be the live data
	X_live = pd.DataFrame([], index=[0]) 
	
	# from here on we draw the widget based on the variable type (numerical or categorical)
	# and set initial values
	with col1:
		feature = "TotalSF"
		st_widget = st.number_input(
			label= feature,
			min_value= int(df[feature].min()*percentageMin), 
			max_value= int(df[feature].max()*percentageMax),
			value= int(df[feature].median()), 
            step= 50
			)
	X_live[feature] = st_widget


	with col2:
		feature = "GarageArea"
		st_widget = st.number_input(
			label= feature,
			min_value= int(df[feature].min()*percentageMin), 
			max_value= int(df[feature].max()*percentageMax),
			value= int(df[feature].median()), 
            step= 50
			)
	X_live[feature] = st_widget


	with col3:
		feature = "YearBuilt"
		st_widget = st.number_input(
			label= feature,
			min_value= int(df[feature].min()*percentageMin), 
			max_value= date.today().year,
			value= int(df[feature].median()), 
            step= 1
			)
	X_live[feature] = st_widget

	with col4:
		feature = "KitchenQual"
		st_widget = st.number_input(
			label= feature,
			min_value= 0, 
			max_value= 10,
			value= int(df[feature].median()), 
            step = 1       
			)
	X_live[feature] = st_widget

	with col5:
		feature = "YearRemodAdd"
		st_widget = st.number_input(
			label= feature,
			min_value= int(df[feature].min()*percentageMin), 
			max_value= date.today().year,
			value= int(df[feature].median()), 
            step= 1
			)
	X_live[feature] = st_widget

	# st.write(X_live)

	return X_live