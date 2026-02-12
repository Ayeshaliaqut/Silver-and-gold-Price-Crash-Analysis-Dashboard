import pandas as pd

def compute_returns(df):
    df["Silver_Return"] = df["SLV"].pct_change()
    df["Gold_Return"] = df["GLD"].pct_change()
    df["DXY_Return"] = df["DXY"].pct_change()
    return df.dropna()

def calculate_rolling_volatility(df, window=30):
    df["Silver_Volatility"] = df["Silver_Return"].rolling(window).std()
    df["Gold_Volatility"] = df["Gold_Return"].rolling(window).std()
    return df

def detect_crashes(df, threshold=-0.03):
    df["Crash"] = df["Silver_Return"] < threshold
    return df

def calculate_correlation(df):
    return df["Silver_Return"].corr(df["DXY_Return"])
