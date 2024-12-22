import pandas as pd

def calculate_indicators(data):
    """Calculates technical indicators (SMA, EMA, etc.)."""
    df = pd.DataFrame.from_dict(data, orient='index')
    df.index = pd.to_datetime(df.index)

    # Convert columns to numeric
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # Calculate indicators (examples)
    df['SMA_50'] = df['4. close'].rolling(window=50).mean()
    df['SMA_200'] = df['4. close'].rolling(window=200).mean()

    # ... add more indicators as needed ...

    # Convert DataFrame back to a dictionary for JSON serialization
    return df.to_dict(orient='index')