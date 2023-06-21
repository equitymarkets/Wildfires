



let defaultURL4 = "/heatmap";
d3.json(defaultURL4).then(function(heat_data) {
  console.log(heat_data)

  let map_data = heat_data;

//Create tile layer 
let baseLayer = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
  maxZoom: 18
});

let points = {
  // radius should be small ONLY if scaleRadius is true (or small radius is intended)
  // if scaleRadius is false it will be the constant radius used in pixels
  "radius": 1,
  "maxOpacity": .8,
  // scales the radius based on map zoom
  "scaleRadius": true,
  // if set to false the heatmap uses the global maximum for colorization
  // if activated: uses the data maximum within the current map boundaries
  //   (there will always be a red spot with useLocalExtremas true)
  "useLocalExtrema": true,
  // which field name in your data represents the latitude - default "lat"
  latField: 'lat',
  // which field name in your data represents the longitude - default "lng"
  lngField: 'lon',
  // which field name in your data represents the data value - default "value"
  valueField: 'size'
};


let heatmapLayer =  new HeatmapOverlay(points);

heatmapLayer.setData(map_data);


//Create map object
let myMap = L.map("map", {
  center: [39.8283, -98.5795],
  zoom: 4,
  layers: [baseLayer, heatmapLayer]
});

// // control that shows state info on hover
let title = L.control();

title.onAdd = function () {
  this._div = L.DomUtil.create('div', 'info');
  this.update();
  return this._div;
};

title.update = function () {
  this._div.innerHTML = '<h4>Heat Map of US Wildfires<br />Year: 2020</h4>';
};

title.addTo(myMap);

});



//----------------------------------------------------------------------------------------------------------->
