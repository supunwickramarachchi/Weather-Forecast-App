import streamlit as st
import plotly.express as px

st.title("Weather Forcast for the Next Days")

place = st.text_input("Place: ")

days = st.slider("Forcast Days", min_value=1, max_value=5, help="Select the number of forecasted days")

option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")

def get_data(select_date):
    dates = ["2024-03-15", "2024-03-16", "2024-03-17", "2024-03-18"]
    temperature = [20, 22, 25, 31]
    temperature = [days * i for i in temperature]
    return dates, temperature


date_list, temperature_list = get_data(days)

figure = px.line(x=date_list, y=temperature_list, labels={"x": "Dates", "y": "Temperature (C)"})
st.plotly_chart(figure)
