"""
Data visualization tools for StockAnalyzer.
"""

import matplotlib.pyplot as plt
import plotly.graph_objs as go
from .config import DEFAULT_STOCKS


def plot_price_trend(prices, symbol=None, period="5y"):
    """
    Plot historical price trend for a single stock symbol.
    Args:
        prices (DataFrame): Price data for the stock.
        symbol (str or None): Stock symbol. If None, use default.
        period (str): Period for historical data.
    """
    if symbol is None:
        symbol = DEFAULT_STOCKS[0]
    if prices is None or prices.empty:
        print(f"No price data to plot for {symbol}.")
        return
    import matplotlib.pyplot as plt
    plt.figure(figsize=(10, 5))
    plt.plot(prices.index, prices['Close'], label=f'{symbol} Close Price')
    plt.title(f'{symbol} Price Trend ({period})')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.tight_layout()
    plt.show()


def plot_financial_ratios(ratios, symbol=None):
    """
    Visualize financial ratios for a single stock symbol.
    Args:
        ratios (dict): Financial indicators for the stock.
        symbol (str or None): Stock symbol. If None, use default.
    """
    if symbol is None:
        symbol = DEFAULT_STOCKS[0]
    if not ratios:
        print(f"No ratios to display for {symbol}.")
        return
    print(f"\nFinancial Ratios for {symbol}:")
    for k, v in ratios.items():
        print(f"  {k}: {v}")
