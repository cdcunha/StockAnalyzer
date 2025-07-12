"""
Export and save functionality for StockAnalyzer.
"""

import pandas as pd
from .config import DEFAULT_STOCKS


def export_to_csv(data, filename, symbol=None):
    """
    Export stock data to CSV for a single stock symbol.
    Args:
        data (DataFrame or dict): Data for the stock.
        filename (str): Output CSV filename.
        symbol (str or None): Stock symbol. If None, use default.
    """
    if symbol is None:
        symbol = DEFAULT_STOCKS[0]
    if data is None:
        print(f"No data to export for {symbol}.")
        return
    try:
        if isinstance(data, pd.DataFrame):
            data.to_csv(filename)
        elif isinstance(data, dict):
            pd.DataFrame([data]).to_csv(filename, index=False)
        print(f"Exported data for {symbol} to {filename}")
    except Exception as e:
        print(f"Error exporting data for {symbol} to CSV: {e}")


def export_to_pdf(report, filename, symbol=None):
    """
    Export analysis/report to PDF for a single stock symbol.
    Args:
        report (str or dict): Report for the stock.
        filename (str): Output PDF filename.
        symbol (str or None): Stock symbol. If None, use default.
    """
    if symbol is None:
        symbol = DEFAULT_STOCKS[0]
    # PDF export stub: You can implement this with ReportLab, FPDF, or similar libraries.
    print(f"[STUB] Would export report for {symbol} to PDF at {filename}.")
    # Example future code:
    # from fpdf import FPDF
    # pdf = FPDF()
    # pdf.add_page()
    # pdf.set_font('Arial', 'B', 12)
    # pdf.multi_cell(0, 10, str(report))
    # pdf.output(filename)
