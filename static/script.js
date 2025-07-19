let map;
let userMarker;

function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    zoom: 13,
    center: { lat: 51.5074, lng: -0.1278 },
  });

  fetch("/cczone")
    .then((res) => res.json())
    .then((data) => {
      const coords = data.features[0].geometry.coordinates[0].map(
        (pt) => ({ lat: pt[1], lng: pt[0] })
      );

      const zonePolygon = new google.maps.Polygon({
        paths: coords,
        strokeColor: "#FF0000",
        strokeOpacity: 0.8,
        strokeWeight: 2,
        fillColor: "#FF0000",
        fillOpacity: 0.2,
      });

      zonePolygon.setMap(map);

      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition((position) => {
          const userPos = {
            lat: position.coords.latitude,
            lng: position.coords.longitude,
          };

          userMarker = new google.maps.Marker({
            position: userPos,
            map: map,
            title: "You are here",
            icon: "http://maps.google.com/mapfiles/ms/icons/blue-dot.png"
          });

          map.setCenter(userPos);

          const inside = google.maps.geometry.poly.containsLocation(
            new google.maps.LatLng(userPos.lat, userPos.lng),
            zonePolygon
          );

          if (inside) {
            alert("⚠️ You're inside the Congestion Charge Zone!");
          }
        });
      }
    });
}

window.onload = initMap;
