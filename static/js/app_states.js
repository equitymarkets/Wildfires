// Plot the default route once the page loads
let defaultURL2 = "/acre/2020";
d3.json(defaultURL2).then(function(bar) {
  console.log(bar)
  //var data = [data];
  
  let xvalues2 = bar.x;
  let yvalues2 = bar.y;
  let trace2 = {
    x: xvalues2,
    y: yvalues2,
    type: 'bar',
    marker: {
      color: '#078B47'
    }
    
  };

  let data = [trace2];
  let layout = {autoscaleYAxis: true,
  title: "United States Total Acreage Burned (Top 10 States)",
xaxis: {
  title: 'US States'
},
yaxis:{
  title: 'Total Acres Burned'
} };
var config = {responsive: true}

  Plotly.plot("bar", data, layout, config);
});

// Update the plot with new data
function updatePlotly2(newdata) {
  Plotly.restyle("bar", "x", [newdata.x]);
  Plotly.restyle("bar", "y", [newdata.y]);
}

// Get new data whenever the dropdown selection changes
function getData2(route) {
  console.log(route);
  if (route === "acre") {
    d3.json(`/${route}`).then(function(data) {
    console.log("newdata", data);
    updatePlotly2(data);
    });
  } else {  
    d3.json(`/acre/${route}`).then(function(data) {
    console.log("newdata", data);
    updatePlotly2(data);
    });
  }

}