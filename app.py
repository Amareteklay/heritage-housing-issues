import streamlit as st
from app_pages.multipage import MultiPage

app = MultiPage(app_name= "Housing Prices") # Create an instance of the app 


app.run() # Run the  app
