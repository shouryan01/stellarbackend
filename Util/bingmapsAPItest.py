import requests

x = requests.get("https://dev.virtualearth.net/REST/v1/Routes/SnapToRoad?points=47.590868,-122.336729;47.601604,-122.336042;47.60849,-122.34241;47.610568,-122.345064&includeTruckSpeedLimit=true&IncludeSpeedLimit=true&speedUnit=MPH&travelMode=driving&key=ApB3pE4UR5Px4wJangIVFcsZGmLzxlHvntQeam933MqxSW4aqIme9SaZO1T_XECy")
print(x, x.json())