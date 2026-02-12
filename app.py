import streamlit as st
import matplotlib.pyplot as plt

from utils.data_loader import (
    load_price_data,
    load_dollar_index,
    merge_datasets
)

from utils.metrics import (
    compute_returns,
    calculate_rolling_volatility,
    detect_crashes,
    calculate_correlation
)

st.set_page_config(page_title="Silver Crash Analysis", layout="wide")

st.title("Silver Price Crash Analysis Dashboard")

price_df = load_price_data()
dxy_df = load_dollar_index()
data = merge_datasets(price_df, dxy_df)

data = compute_returns(data)
data = calculate_rolling_volatility(data)
data = detect_crashes(data)

st.header("Market Overview")

plt.figure()
plt.plot(data["Date"], data["SLV"], label="Silver")
plt.plot(data["Date"], data["GLD"], label="Gold")
plt.legend()
st.pyplot(plt)

st.markdown("""
Silver exhibits sharper price swings compared to gold,
indicating higher inherent market sensitivity.
""")

st.header("Volatility & Risk Analysis")

plt.figure()
plt.plot(data["Date"], data["Silver_Volatility"], label="Silver Volatility")
plt.plot(data["Date"], data["Gold_Volatility"], label="Gold Volatility")
plt.legend()
st.pyplot(plt)

st.markdown("""
Silver consistently shows higher rolling volatility than gold.
Volatility spikes often precede major price declines,
highlighting increased crash vulnerability.
""")

st.header("Crash Event Detection")

crash_days = data[data["Crash"]]

plt.figure()
plt.plot(data["Date"], data["SLV"], label="Silver Price")
plt.scatter(crash_days["Date"], crash_days["SLV"], marker="o")
plt.legend()
st.pyplot(plt)

st.write("Number of detected crash days:", len(crash_days))

st.markdown("""
Crash events are defined as daily drops greater than 3%.
These events cluster during high-volatility regimes.
""")

st.header("Dollar Strength Impact")

correlation = calculate_correlation(data)
st.metric("Silver vs Dollar Return Correlation", round(correlation, 3))

plt.figure()
plt.plot(data["Date"], data["DXY"], label="Dollar Index")
plt.plot(data["Date"], data["SLV"], label="Silver")
plt.legend()
st.pyplot(plt)

st.markdown("""
A stronger dollar often pressures silver prices downward.
The negative correlation indicates macroeconomic sensitivity.
""")

st.markdown("""
---
This dashboard is for educational and analytical purposes only.
It does not provide financial advice or price predictions.
""")
