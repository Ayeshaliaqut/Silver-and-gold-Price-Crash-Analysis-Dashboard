import pandas as pd

def load_price_data():
    df = pd.read_csv("data/gld_price_data.csv")
    df["Date"] = pd.to_datetime(df["Date"])
    df = df[["Date", "GLD", "SLV"]]
    df = df.dropna()
    return df

def load_dollar_index():
    dxy = pd.read_csv("data/US Dollar Index Historical Data.csv")
    dxy["Date"] = pd.to_datetime(dxy["Date"])
    dxy = dxy[["Date", "Price"]]
    dxy.rename(columns={"Price": "DXY"}, inplace=True)
    dxy = dxy.dropna()
    return dxy

def merge_datasets(price_df, dxy_df):
    merged = pd.merge(price_df, dxy_df, on="Date", how="inner")
    return merged
