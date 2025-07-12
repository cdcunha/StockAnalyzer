"""
Logging and error handling utilities for StockAnalyzer.
"""

import logging
import sys
import yfinance as yf

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)


def log_error(error_msg):
    """Log an error message."""
    logging.error(error_msg)


def notify_user(message):
    """Provide user-friendly feedback (could be extended for GUI)."""
    print(f"[StockAnalyzer] {message}")


def validate_stock_symbol(symbol):
    """
    Validate if a stock symbol is valid by checking if yfinance returns data.
    Returns True if valid, False otherwise.
    """
    try:
        ticker = yf.Ticker(symbol)
        hist = ticker.history(period="1d")
        return not hist.empty
    except Exception as e:
        log_error(f"Validation failed for symbol {symbol}: {e}")
        return False
