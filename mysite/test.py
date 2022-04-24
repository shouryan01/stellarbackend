import requests

data = [
    {   
        "vin": "76",
        "speed": "67878.000000000000000",
        "speedlimit": "6.000000000000000",
        "longitude": "765.000000000000000",
        "latitude": "85.000000000000000"
    },
    {
        "vin": "86",
        "speed": "67878.000000000000000",
        "speedlimit": "6.000000000000000",
        "longitude": "765.000000000000000",
        "latitude": "85.000000000000000"
    },
    {
        "vin": "96",
        "speed": "67878.000000000000000",
        "speedlimit": "6.000000000000000",
        "longitude": "765.000000000000000",
        "latitude": "85.000000000000000"
    },
    {
        "vin": "106",
        "speed": "67878.000000000000000",
        "speedlimit": "6.000000000000000",
        "longitude": "765.000000000000000",
        "latitude": "85.000000000000000"
    },
    {
        "vin": "726",
        "speed": "67878.000000000000000",
        "speedlimit": "6.000000000000000",
        "longitude": "765.000000000000000",
        "latitude": "85.000000000000000"
    },
    # {"vin": "1C4RJFBGXMC877858", "speed": 0.0, "speedLimit": 0.0, "Latitude": "42.4424723", "Longitude": "-83.0169672"}
]

for i in data:
    x = requests.post("http://localhost:8000/api/data/", data=i)
    print(x)

