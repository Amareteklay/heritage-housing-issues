import streamlit as st

def predict_price(X_live, house_features, price_pipeline):

	# from live data, subset features related to this pipeline
	X_live_price = X_live.filter(house_features)

	# predict
	price_prediction = price_pipeline.predict(X_live_price)
	# st.write(tenure_prediction_proba)

	# create a logic to display the results
	
	statement = (
			f"* The price of a house with the given attribute values is: **{price_prediction[0]}**."
			)
	
	st.write(statement)