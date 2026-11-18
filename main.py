import streamlit as st
import plotly.express as px
import pandas as pd


def get_data(num_days):
    dates = ["2026-11-19", "2026-11-20", "2026-11-21"]
    temperatures = [10, 11, 12]
    temperatures = [num_days * t for t in temperatures]
    return dates, temperatures


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

option = st.selectbox(
    label="Select data to view",
    options=("", "Temperature", "Sky"),
    index=0,
    required=True,
    key="option")

if place and option:
    st.subheader(
        body=f"{option.title()} for the next {num_days} "
             f"day{'' if num_days == 1 else 's'} in {place.title()}",
        text_alignment="center")

    d, t = get_data(num_days)

    figure = px.line(
        x=d,
        y=t,
        labels={"x": "Date", "y": "Temperature °C"})

    st.plotly_chart(figure)

