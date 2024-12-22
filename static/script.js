// script.js

function fetchData(stockSymbol) {
    fetch(`/api/data/${stockSymbol}`)
        .then(response => response.json())
        .then(data => {
            // Process the data and update the charts using a JavaScript charting library
            // For example, you can use Plotly.js to create interactive charts
            createPlotlyChart(data);
        })
        .catch(error => {
            console.error('Error fetching data:', error);
        });
}

function createPlotlyChart(data) {
    // Process your data into a format suitable for Plotly
    const trace = {
        x: data.map(item => item.date),
        close: data.map(item => item.close),
        decreasing: {line: {color: '#7F7F7F'}},
        high: data.map(item => item.high),
        increasing: {line: {color: '#17BECF'}},
        line: {color: 'rgba(31,119,180,1)'},
        low: data.map(item => item.low),
        open: data.map(item => item.open),
        type: 'candlestick',
        xaxis: 'x',
        yaxis: 'y'
    };

    const plotlyData = [trace];

    const layout = {
        dragmode: 'zoom',
        margin: {
            r: 10,
            t: 25,
            b: 40,
            l: 60
        },
        showlegend: false,
        xaxis: {
            autorange: true,
            domain: [0, 1],
            range: ['2023-01-01', '2024-03-18'], // adjust the range accordingly
            rangeslider: {range: ['2023-01-01', '2024-03-18']}, // adjust the range accordingly
            title: 'Date',
            type: 'date'
        },
        yaxis: {
            autorange: true,
            domain: [0, 1],
            range: [114.66, 137.8], 
            type: 'linear'
        }
    };

    Plotly.newPlot('chart-container', plotlyData, layout);
}


// Example: Fetch data for a stock when the page loads
window.onload = () => {
    fetchData('AAPL'); // Fetch data for Apple stock
};