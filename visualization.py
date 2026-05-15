import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


def line_chart(df):
    st.subheader("Temperature Line Chart")

    fig, ax = plt.subplots()

    ax.plot(df["City"], df["Temperature"], marker='o')

    ax.set_xlabel("City")
    ax.set_ylabel("Temperature (°C)")
    ax.set_title("City vs Temperature")

    st.pyplot(fig)


def bar_chart(df):
    st.subheader("Humidity Bar Chart")

    fig, ax = plt.subplots()

    sns.barplot(x="City", y="Humidity", data=df, ax=ax)

    ax.set_title("City vs Humidity")

    st.pyplot(fig)


def heatmap(df):
    st.subheader("Weather Heatmap")

    heatmap_data = df[["Temperature", "Humidity", "Wind Speed"]]

    fig, ax = plt.subplots()

    sns.heatmap(heatmap_data.corr(), annot=True, cmap="coolwarm", ax=ax)

    st.pyplot(fig)


def pie_chart(df):
    st.subheader("Weather Condition Distribution")

    weather_counts = df["Weather"].value_counts()

    fig, ax = plt.subplots()

    ax.pie(
        weather_counts,
        labels=weather_counts.index,
        autopct='%1.1f%%'
    )

    ax.set_title("Weather Conditions")

    st.pyplot(fig)