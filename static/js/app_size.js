
        // Fetch histogram data from the backend
        fetch('/size')
            .then(response => response.json())
            .then(data => {
                // Parse the JSON data
                const histogramData = JSON.parse(data);

                // Render the histogram using Plotly.js
                Plotly.newPlot('histogram', histogramData);
            })
            .catch(error => console.error('Error:', error));
