

// window.onload = init;

// function init() {
//   const mapElement = document.getElementById("mapid");
//   var map = L.map(mapElement).setView([35, 9.5], 5);
//   L.tileLayer("http://{s}.tile.osm.org/{z}/{x}/{y}.png", {
//     attribution:
//       '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
//   }).addTo(map);

//   // FeatureGroup is to store editable layers
//   // var drawnItems = new L.FeatureGroup();
//   // map.addLayer(drawnItems);
//   // var drawEditControl = new L.Control.Draw({
//   //   draw: false,
//   //   edit: {
//   //     featureGroup: drawnItems,
//   //   },
//   // });
//   // var drawControl = new L.Control.Draw({
//   //   edit: {
//   //     featureGroup: drawnItems,
//   //   },
//   // });
//   // map.addControl(drawControl);

//   // var coordinates = [];

//   // map.on("draw:created, draw:edited", function (e) {
//   //   drawnItems.clearLayers();

//   //   drawnItems.eachLayer(function (layer) {
//   //     coordinates.push(layer.toGeoJSON().geometry.coordinates);
//   //   });

//   //   document.getElementById("points").value = JSON.stringify(coordinates);
//   //   drawnItems.addLayer(e.layer);
//   // });

//   // map.on("draw:deleted", function () {
//   //   coordinates = [];
//   //   drawControl.addTo(map);
//   //   drawEditControl.remove();
//   //   document.getElementById("points").value = "";
//   // });

  
//   var marker;
    
//   map.on("click", function (e) {
//     // If marker is already defined, remove it before adding a new one
//     // if (marker) {
//     //   map.removeLayer(marker);
//     // }
//     // Add new marker at double-clicked location
//     marker = L.marker(e.latlng, { draggable: true }).addTo(map);
//   marker.bindPopup('heloooooooooooooo.')
//       .openPopup();
    
//     document.getElementById("lat").value = e.latlng.lat;
//     document.getElementById("lng").value = e.latlng.lng;
  
//     marker.on("dragend", function (e) {
//       var marker = e.target;
//       var position = marker.getLatLng();
//       document.getElementById("lat").value = position.lat;
//       document.getElementById("lng").value = position.lng;
//     });
//   });
// }

window.onload = init;

function init() {
  const mapElement = document.getElementById("mapid");
  var map = L.map(mapElement).setView([33.5731, -7.5898], 13);

  // var map = L.map(mapElement).setView([35, 9.5], 5 );
  L.tileLayer("http://{s}.tile.osm.org/{z}/{x}/{y}.png", {
    attribution:
      '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
  }).addTo(map);

  var markers = [];

  map.on("click", function (e) {
    var marker = L.marker(e.latlng, { draggable: true }).addTo(map);
    markers.push(marker);

    marker.on("dragend", function (e) {
      var marker = e.target;
      var position = marker.getLatLng();
      document.getElementById("lat").value = Position.lat;
      document.getElementById("lng").value = Position.lng;
    });
  });

  // Remove all markers on the map
  function removeAllMarkers() {
    for (var i = 0; i < markers.length; i++) {
      map.removeLayer(markers[i]);
    }
    markers = [];
  }

  // Retrieve all marker positions
  function getMarkerPositions() {
    var Positions = [];
    for (var i = 0; i < markers.length; i++) {
      Positions.push(markers[i].getLatLng());
    }
    return Positions;
  }

  // Example button to remove all markers and retrieve their positions
  var button = document.createElement("button");
  button.innerHTML = "Remove all markers and retrieve positions";
  button.onclick = function () {
    var positions = getMarkerPositions();
    console.log(Positions);
    removeAllMarkers();
  };
  document.body.appendChild(button);
}
