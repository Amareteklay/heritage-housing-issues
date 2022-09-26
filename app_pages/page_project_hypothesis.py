import streamlit as st

def page_project_hypothesis_body():

    st.write("### Project Hypotheses and Validation")

    # conclusions taken from "02 - Churned Customer Study" notebook 
    st.success(
       f"* Size matters. Variables that are associated with the size of the house are positively correlated to sale price. We will examine correlations between attributes about the size of the house and the sale price.\n\n"
       
       f"* Ratings of the quality and condition of the house reflect its value and thus higher ratings indicate higher sale price. We will use the correlation between variables about the different ratings of the house and the sale price to validate this hypothesis.\n\n"
       
       f"* Age of the house is expected to have significant influence on the sale price of the house. We study when the house was built and how expensive it is to test this hypothesis.\n"
       )
        