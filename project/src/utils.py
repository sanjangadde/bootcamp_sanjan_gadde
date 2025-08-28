import pandas as pd

def get_summary_stats(df):
    return df.describe()

def predict(model, features, round_prediction=False):
    pred = model.predict([features])[0]
    if round_prediction:
        pred = round(pred, 2)
    return pred