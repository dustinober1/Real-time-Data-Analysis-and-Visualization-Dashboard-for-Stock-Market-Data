from flask import Flask, render_template, request, jsonify
from data_fetcher import get_stock_data
from data_analyzer import calculate_indicators

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data', methods=['POST'])
def get_data():
    symbol = request.form['symbol'].upper()  # Get stock symbol from the form and make it uppercase
    data = get_stock_data(symbol)
    if data:
        analyzed_data = calculate_indicators(data)
        return jsonify(analyzed_data)
    else:
        return jsonify({'error': 'Invalid stock symbol or API error'}), 400  # Return error with status code 400

if __name__ == '__main__':
    app.run(debug=True)