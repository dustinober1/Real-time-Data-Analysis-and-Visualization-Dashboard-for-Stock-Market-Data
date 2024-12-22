import yfinance as yf

def get_stock_data(symbol):
    """Fetches real-time or historical stock data using yfinance."""
    ticker = yf.Ticker(symbol)
    data = ticker.history()  # You can add parameters like period, interval, etc.
    # Convert the data to a format similar to your previous API response
    processed_data = {
        'date': data.index.tolist(),
        'open': data['Open'].tolist(),
        'high': data['High'].tolist(),
        'low': data['Low'].tolist(),
        'close': data['Close'].tolist(),
        # ... other necessary data
    }
    return processed_data