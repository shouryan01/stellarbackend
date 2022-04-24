from score import get_score
import requests

curr_score = requests.get("http://127.0.0.1:8000/api/drivers/2/").json()["score"]
# print(curr_score)

data = {
    "username": "shouryan",
    "score": curr_score - get_score()
}

x = requests.put("http://127.0.0.1:8000/api/drivers/2/", data=data)
print(x, x.json())