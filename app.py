import streamlit as st
from datetime import datetime

from weather_api import fetch_weather
from data_processing import create_dataframe, clean_data, basic_analysis
from visualization import (
    line_chart,
    bar_chart,
    heatmap,
    pie_chart
)

# Streamlit page configuration
st.set_page_config(
    page_title="Weather Dashboard",
    layout="wide"
)
# Sidebar
st.sidebar.title("🌦 Weather Dashboard")

st.sidebar.write("API Integration Project")

st.sidebar.write("Using:")
st.sidebar.write("- Python")
st.sidebar.write("- OpenWeatherMap API")
st.sidebar.write("- Streamlit")
st.sidebar.write("- Matplotlib")
st.sidebar.write("- Seaborn")
st.title("🌦 Weather Data Visualization Dashboard")

st.write("Real-time Weather Analysis using OpenWeatherMap API")
st.write("Last Updated:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
# List of cities
cities = [
    "Delhi",
    "Mumbai",
    "Kolkata",
    "Chennai",
    "Bangalore",
    "Hyderabad"
]

weather_data_list = []
#fetch weather data for each city
with st.spinner("Fetching weather data..."):

    for city in cities:

        data = fetch_weather(city)

        if data:
            weather_data_list.append(data)

# Create DataFrame
df = create_dataframe(weather_data_list)

# Clean data
df = clean_data(df)

# Show raw data
st.subheader("Weather Data Table")

if not df.empty:
    st.dataframe(df)
    
else:
    st.error("Weather data table is empty.")


# Basic analysis
# Metrics

col1, col2, col3 = st.columns(3)

col1.metric(
    "Average Temperature",
    f"{df['Temperature'].mean():.2f} °C"
)

col2.metric(
    "Average Humidity",
    f"{df['Humidity'].mean():.2f}%"
)

col3.metric(
    "Average Wind Speed",
    f"{df['Wind Speed'].mean():.2f} m/s"
)
st.subheader("Statistical Summary")

if not df.empty:
    st.write(df.describe())
else:
    st.error("No weather data available. Check your API key or internet connection.")

# Visualizations
line_chart(df)

bar_chart(df)

heatmap(df)

pie_chart(df)

# Footer
st.markdown("---")
st.write("Created using Python, Streamlit, Matplotlib, and Seaborn")

st.write("Developed By: Tuhin Roy")

st.write("Internship Project - CodTech")

st.write("Intern ID: CTIS05SQ")