import streamlit as st
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


option = st.selectbox(
    label="Select data to view",
    options=("", "Temperature", "Sky"),
    index=0,
    required=True,
    key="option")

if option:
    st.subheader(
        body=f"{option.title()} for the next {num_days} "
             f"day{'' if num_days == 1 else 's'} in {place.title()}",
        text_alignment="center")
