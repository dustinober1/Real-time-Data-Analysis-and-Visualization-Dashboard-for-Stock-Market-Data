from flask import Flask, render_template, jsonify
from data_fetcher import get_stock_data
from data_analyzer import calculate_indicators
# from visualizer import create_chart (if separated)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data/<stock_symbol>')
def get_data(stock_symbol):
    data = get_stock_data(stock_symbol)
    analyzed_data = calculate_indicators(data)
    # chart_data = create_chart(analyzed_data) (if separated)

    # You might send processed data directly to the frontend for
    # client-side charting with a JS library or send pre-generated
    # chart data (e.g., base64 encoded image or JSON for Plotly)

    return jsonify(analyzed_data)

if __name__ == '__main__':
    app.run(debug=True)