import streamlit as st
import plotly.express as px

st.title("Weather Forcast for the Next Days")

place = st.text_input("Place: ")

days = st.slider("Forcast Days", min_value=1, max_value=5, help="Select the number of forecasted days")

option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")


