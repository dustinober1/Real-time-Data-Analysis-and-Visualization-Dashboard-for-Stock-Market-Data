document.getElementById('stock-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission

    const symbol = document.getElementById('symbol').value;

    fetch('/api/data', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `symbol=${symbol}`
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Invalid stock symbol or API error');
        }
        return response.json();
    })
    .then(data => {
        // Process the data and update the charts using Plotly
        createPlotlyChart(data);
    })
    .catch(error => {
        console.error('Error:', error);
        alert(error.message); // Display error message to the user
    });
});

function createPlotlyChart(data) {
    const dates = Object.keys(data);
    const closePrices = Object.values(data).map(item => item['4. close']);

    const trace = {
        x: dates,
        y: closePrices,
        type: 'scatter', // Or 'candlestick' for a more detailed chart
        mode: 'lines+markers',
        name: 'Closing Price'
    };

    const layout = {
        title: `Stock Price Data`,
        xaxis: {
            title: 'Date'
        },
        yaxis: {
            title: 'Closing Price'
        }
    };

    Plotly.newPlot('chart-container', [trace], layout);
}