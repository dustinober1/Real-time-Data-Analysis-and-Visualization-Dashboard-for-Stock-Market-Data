import requests

def get_stock_data(symbol):
    """
    Fetches stock data from the Alpha Vantage API for the given symbol.

    Args:
        symbol (str): The stock symbol (e.g., AAPL, MSFT).

    Returns:
        dict: The time series data (daily adjusted) as a dictionary, 
              or None if an error occurred.
    """

    api_key_file = "/Users/dustinober/api_key.txt"  # Path to your API key file
    try:
        with open(api_key_file, "r") as f:
            api_key = f.read().strip()  # Read the key and remove leading/trailing whitespace
    except FileNotFoundError:
        print(f"Error: API key file not found at {api_key_file}")
        return None

    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={api_key}&outputsize=compact"

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        # Print the entire API response for debugging (you can remove this later)
        print("Full API Response:", data)

        # Check for API errors (updated error handling)
        if "Error Message" in data:
            print(f"API Error: {data['Error Message']}")
            return None
        elif "Information" in data and "Thank you for using Alpha Vantage" in data["Information"]:
            # API call frequency limit
            print(f"API Limit Reached: {data['Information']}")
            return None
        elif "Time Series (Daily)" not in data:
            print(f"Unexpected API Response: No time series data found.")
            return None

        # Extract relevant time series data
        time_series = data["Time Series (Daily)"]
        return time_series

    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")
        return None
    except (KeyError, ValueError) as e:
        print(f"Data Parsing Error: {e}")
        return None