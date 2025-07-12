"""
Configuration and default values for StockAnalyzer.
"""

# Default stocks for analysis
DEFAULT_STOCKS = [
    'FSELX', 'ITUB', 'SHLS', 'CHRD', 'VALE',
    'FLJH', 'AAPL', 'TM', 'MSFT', 'JPM', 'AMZN'
]


def get_stocks_to_analyze(user_stocks=None):
    """
    Return the list of stocks to analyze.
    If user_stocks is provided and not empty, use it. Otherwise, use DEFAULT_STOCKS.
    """
    if user_stocks and isinstance(user_stocks, (list, tuple)) and len(user_stocks) > 0:
        return user_stocks
    return DEFAULT_STOCKS
