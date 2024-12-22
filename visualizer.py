import plotly.graph_objects as go
import pandas as pd

def create_chart(data):
    """Creates an interactive chart using Plotly."""
    df = pd.DataFrame(data)

    fig = go.Figure(data=[go.Candlestick(
        x=df['date'],
        open=df['open'],
        high=df['high'],
        low=df['low'],
        close=df['close']
    )])

    fig.update_layout(
        title='Stock Price Chart',
        yaxis_title='Stock Price'
    )

    # Convert the figure to JSON or HTML for embedding in the web page
    chart_json = fig.to_json()
    # or chart_html = fig.to_html()

    return chart_json