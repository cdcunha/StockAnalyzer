"""
Stock data retrieval and financial indicators for StockAnalyzer.
"""

import yfinance as yf
import pandas as pd
from .config import DEFAULT_STOCKS


def fetch_historical_prices(symbol=None, period="5y"): 
    """
    Fetch historical price data for a single stock symbol.
    Args:
        symbol (str or None): Stock symbol. If None, use default (first in default list).
        period (str): Period for historical data (e.g., '1y', '5y').
    Returns:
        DataFrame or None
    """
    if symbol is None:
        symbol = DEFAULT_STOCKS[0]
    try:
        df = yf.download(symbol, period=period)
        if df.empty:
            return None
        return df
    except Exception as e:
        print(f"Error fetching historical prices for {symbol}: {e}")
        return None


def fetch_financial_indicators(symbol=None):
    """
    Fetch key financial indicators (PE ratio, market cap, revenue, etc.) for a single stock symbol.
    Args:
        symbol (str or None): Stock symbol. If None, use default (first in default list).
    Returns:
        dict or None
    """
    if symbol is None:
        symbol = DEFAULT_STOCKS[0]
    try:
        ticker = yf.Ticker(symbol)
        info = ticker.info
        # Extract key indicators
        indicators = {
            'symbol': symbol,
            'shortName': info.get('shortName'),
            'sector': info.get('sector'),
            'marketCap': info.get('marketCap'),
            'trailingPE': info.get('trailingPE'),
            'forwardPE': info.get('forwardPE'),
            'priceToBook': info.get('priceToBook'),
            'revenue': info.get('totalRevenue'),
            'grossMargins': info.get('grossMargins'),
            'dividendYield': info.get('dividendYield'),
        }
        return indicators
    except Exception as e:
        print(f"Error fetching indicators for {symbol}: {e}")
        return None
