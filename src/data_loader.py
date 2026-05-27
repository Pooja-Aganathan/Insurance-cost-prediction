import pandas as pd


def load_data():

    df = pd.read_csv("data/raw/insurance_cost_prediction_data.csv")

    return df
