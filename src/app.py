import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.config import DEFAULT_STOCKS
from src.utils import validate_stock_symbol
from src.fetch_data import fetch_historical_prices, fetch_financial_indicators
from src.visualization import plot_price_trend, plot_financial_ratios
from src.export import export_to_csv

st.set_page_config(page_title="StockAnalyzer", layout="wide")
st.title("📈 StockAnalyzer")
st.write("Analyze stocks, view financials, and export your results!")

option = st.radio("Choose stock input method:", ["Pick from default", "Type your own"])
if option == "Pick from default":
    symbol = st.selectbox("Select a stock:", DEFAULT_STOCKS)
    valid = True
else:
    symbol = st.text_input("Enter stock symbol:").strip().upper()
    valid = validate_stock_symbol(symbol) if symbol else False
    if symbol and not valid:
        st.error(f"'{symbol}' is not a valid stock symbol.")

if valid and symbol:
    st.success(f"Analyzing {symbol}...")
    prices = fetch_historical_prices(symbol)
    indicators = fetch_financial_indicators(symbol)
    with st.expander("Price Trend Chart", expanded=True):
        if prices is not None:
            import matplotlib.pyplot as plt
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.plot(prices.index, prices['Close'], label=f'{symbol} Close Price')
            ax.set_title(f"{symbol} Price Trend (5y)")
            ax.set_xlabel('Date')
            ax.set_ylabel('Price (USD)')
            ax.legend()
            st.pyplot(fig)
        else:
            st.warning("No price data found.")
    with st.expander("Financial Ratios and Key Metrics", expanded=True):
        if indicators:
            st.json(indicators)
        else:
            st.warning("No indicators found.")
    st.markdown("---")
    st.subheader("Export Data")
    csv_filename = f"{symbol}_prices.csv"
    if st.button("Export price data to CSV"):
        export_to_csv(prices, csv_filename, symbol)
        st.success(f"Exported price data to {csv_filename}")
    # PDF export stub
    st.button("Export analysis to PDF (coming soon)")
