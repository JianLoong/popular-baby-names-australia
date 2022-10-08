(function() {

    var map = L.map('map', {
    });
  
  
    $.getJSON("./states.geojson", function(data) {
    
      var geojson = L.geoJson(data, {

        onEachFeature: function (feature, layer) {
          layer.bindPopup(feature.properties['STATE_NAME']);
  
          layer
          .on('mouseover', function(e) {
            layer.setStyle({
              weight: 4,
              fillOpacity: 0.8
            });
            info.update(layer.feature.properties);
          })
          .on('mouseout', function(e) {
            geojson.resetStyle(layer);
            info.update();
          })
        }
      })
  
      geojson.addTo(map);
      var bounds = geojson.getBounds();
  
      map.fitBounds(bounds);
  
      map.options.maxBounds = bounds;
      map.options.minZoom = map.getZoom();
    });
  
  })();