"""
Financial report retrieval (10-K, 10-Q) for StockAnalyzer.
"""

from sec_edgar_downloader import Downloader
import os
from .config import DEFAULT_STOCKS


def download_sec_report(symbol=None, report_type="10-K", save_dir="./data/reports"):
    """
    Download SEC filings for a single stock symbol.
    Args:
        symbol (str or None): Stock symbol. If None, use default.
        report_type (str): SEC report type (e.g., '10-K', '10-Q').
        save_dir (str): Directory to save reports.
    """
    if symbol is None:
        symbol = DEFAULT_STOCKS[0]
    # Placeholder for actual SEC download code
    # dl = Downloader(save_dir)
    # dl.get(report_type, symbol)
    pass
