import streamlit as st
import plotly.express as px
from backend import get_weather_data
import pandas as pd

# st.set_page_config(layout="wide")

st.title(body="Weather Forecast for the Next Days", text_alignment="center")

place = st.text_input(
    label="Place:",
    placeholder="Enter City Name",
    required=True,
    key="place")

num_days = st.slider(
    label="Forecast Days",
    min_value=1,
    max_value=5,
    value=1,
    key="num_days",
    help="Select the number of days to forecast")

report_kind = st.selectbox(
    label="Select data to view",
    options=("", "Temperature", "Sky"),
    index=0,
    required=True,
    key="option")

if place and report_kind:
    st.subheader(
        body=f"{report_kind.title()} for the next {num_days} "
             f"day{'' if num_days == 1 else 's'} in {place.title()}",
        text_alignment="center")

    data = get_weather_data(place, num_days)

    d, t, w = data

    if report_kind == "Temperature":
        figure = px.scatter(
            x=d,
            y=t,
            labels={"x": "Date", "y": "Temperature °C"})

        st.plotly_chart(figure)
    elif report_kind == "Sky":
        for i in w:
            st.write(f"{i[0]} => {i[1]}")

