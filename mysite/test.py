import requests

data = {
        "id": 4,
        "username": "muhaddatha",
        "age": 18,
        "score": 700,
        "state": "OH",
        "team": 1001,
        "make": "Chrysler",
        "year": 2020,
    }

x = requests.post("http://localhost:8000/api/drivers/", data=data)
print(x, x.json())