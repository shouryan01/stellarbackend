import requests
import random
import names

for i in range(8, 92):
    data = {
        "id": 5,
        "username": names.get_first_name(),
        "age": random.randint(18, 65),
        "score": random.randint(300, 850),
        "state": random.choice(['MI', 'IN', 'WI', 'OH', 'IL', 'PA', 'NY', 'MN']),
        "team": random.randint(1002, 1010),
        "make": random.choice(['Chrysler', 'Dodge', 'Jeep', 'Ram']),
        "year": random.randint(2000, 2022),
        "groups": []
    }
    x = requests.post("http://127.0.0.1:8000/api/drivers/", data = data)
    print(x, x.json())