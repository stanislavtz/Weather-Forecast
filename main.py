import streamlit as st
import plotly.express as px
from backend import get_weather_data
import datetime

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
    try:
        st.subheader(
            body=f"{report_kind.title()} for the next {num_days} "
                 f"day{'' if num_days == 1 else 's'} in {place.title()}",
            text_alignment="center")

        data = get_weather_data(place, num_days)

        dates, temperatures, weathers = data

        match report_kind:
            case "Temperature":
                figure = px.scatter(
                    x=dates,
                    y=temperatures,
                    labels={"x": "Date", "y": "Temperature °C"})

                st.plotly_chart(figure)
            case "Sky":
                cols = st.columns(len(weathers))
                for col, weather in zip(cols, weathers):
                    w = ""
                    if "Sunny" in weather[1]:
                        w = "clear"
                    elif "Cloudy" in weather[1]:
                        w = "cloud"
                    elif "Showers" in weather[1]:
                        w = "rain"
                    elif "Snow" in weather[1]:
                        w = "snow"

                    d = datetime.datetime.fromisoformat(weather[0])
                    with col:
                        st.image(f"images/{w}.png", width=100, caption=d.strftime('%d-%m-%Y'))
    except AttributeError:
        st.warning("That place not exist!")
