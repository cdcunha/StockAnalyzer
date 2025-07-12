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
    Returns:
        str: Path to downloaded report or None
    """
    if symbol is None:
        symbol = DEFAULT_STOCKS[0]
    try:
        os.makedirs(save_dir, exist_ok=True)
        dl = Downloader(save_dir)
        dl.get(report_type, symbol)
        # Find the newest file in the directory for this symbol and report_type
        report_dir = os.path.join(save_dir, report_type, symbol)
        if not os.path.isdir(report_dir):
            return None
        files = sorted(
            [os.path.join(report_dir, f) for f in os.listdir(report_dir)],
            key=os.path.getmtime,
            reverse=True
        )
        return files[0] if files else None
    except Exception as e:
        print(f"Error downloading SEC report for {symbol}: {e}")
        return None
