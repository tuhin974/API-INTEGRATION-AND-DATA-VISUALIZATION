import pandas as pd


def create_dataframe(weather_list):
    """
    Convert weather data list into DataFrame
    """

    df = pd.DataFrame(weather_list)

    return df


def clean_data(df):
    """
    Clean and preprocess data
    """

    df.dropna(inplace=True)

    return df


def basic_analysis(df):
    """
    Display basic statistics
    """

    print("\nBasic Statistics:\n")
    print(df.describe())