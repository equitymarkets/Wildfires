let defaultURL5 = "/PopData";
d3.json(defaultURL5).then(function(pop_data) {
  console.log(pop_data)

let map = L.map('map2').setView([37.8, -96], 4);
//sets the layer that sits below everything, i.e. streets and other features
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
		maxZoom: 19,
		attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
	}).addTo(map); 


	let info = L.control();

	info.onAdd = function (map) {
		this._div = L.DomUtil.create('div', 'info');
		this.update();
		return this._div;
	};


	info.update = function (props) {
        const contents = props ? `<b>${props.name}</b><br />&#x2022; 2020 density: ${props.density} people / mi<sup>2</sup></b><br />&#x2022; 1990-2020 Change: ${props.density_change}%` : 'Hover over a state';
        this._div.innerHTML = `<h4>US Population Density Change 1992-2020</h4>${contents}`;
    };
	info.addTo(map);


	// get color depending on population density value
	function getColor(d) {
		return d > 100 ? '#99000d' :
			d > 50  ? '#cb181d' :
			d > 25   ? '#fb6a4a' :
			d > 10   ? '#fcbba1' :
			d < 0   ? '#fee0d2' : '#fff5f0';
	}

	function style(feature) {
		return {
			weight: 2,
			opacity: 1,
			color: 'white',
			dashArray: '3',
			fillOpacity: 0.7,
			fillColor: getColor(feature.properties.density_change)
		};
	}

	function highlightFeature(e) {
		const layer = e.target;

		layer.setStyle({
			weight: 5,
			color: '#666',
			dashArray: '',
			fillOpacity: 0.7
		});

		layer.bringToFront();

		info.update(layer.feature.properties);
	}

	// Population density data //
	let geojson = L.geoJson(pop_data, {
		style,
		onEachFeature
	}).addTo(map);

	function resetHighlight(e) {
		geojson.resetStyle(e.target);
		info.update();
	}

	function zoomToFeature(e) {
		map.fitBounds(e.target.getBounds());
	}

	function onEachFeature(feature, layer) {
		layer.on({
			mouseover: highlightFeature,
			mouseout: resetHighlight,
			click: zoomToFeature
		});
	}

	map.attributionControl.addAttribution('Population data &copy; <a href="https://www.census.gov/data/tables/time-series/dec/density-data-text.html">US Census Bureau</a>');


	var legend = L.control({position: 'bottomright'});

	legend.onAdd = function (map) {

		var div = L.DomUtil.create('div', 'info legend');
		var grades = [-5, 10, 25, 50, 100];
		var labels = [];
		let from, to;

		for (let i = 0; i < grades.length; i++) {
			from = grades[i];
			to = grades[i + 1];

			labels.push(`<i style="background:${getColor(from + 1)}"></i> ${from}${to ? `&ndash;${to}` : '+'}`);
		}

		div.innerHTML = labels.join('<br>');
		return div;
	};

	legend.addTo(map)
	
});