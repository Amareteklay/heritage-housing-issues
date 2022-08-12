import streamlit as st

def predict_price(X_live, house_features, price_pipeline, price_labels_map):

	# from live data, subset features related to this pipeline
	X_live_price = X_live.filter(house_features)

	# predict
	price_prediction = price_pipeline.predict(X_live_price)
	price_prediction_proba = price_pipeline.predict_proba(X_live_price)
	# st.write(tenure_prediction_proba)

	# create a logic to display the results
	proba = price_prediction_proba[0,price_prediction][0]*100
	price_levels = price_labels_map[price_prediction[0]]

	if price_prediction != 1:
		statement = (
			f"* In addition, there is a {proba.round(2)}% probability the prospect "
			f"will stay **{price_levels} months**. "
			)
	else:
		statement = (
			f"* The model has predicted the prospect would stay **{price_levels} months**, "
			f"however we acknowledge that the recall and precision levels for {price_levels} is not "
			f"strong. The AI tends to identify potential churners, but for this prospect the AI is not "
			f"confident enough on how long the prospect would stay."
		)
		
	st.write(statement)