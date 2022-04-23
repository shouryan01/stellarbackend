import time
import json, requests



base_url = "https://api.stellantis-developers.com"
headers = {
    "x-api-key": API_KEY, "user": API_USERNAME, "password": API_PASSWORD
}


def get_bearer_token():
    bearer_token_response = requests.post(base_url + "/v1/auth/token", headers=headers)
    response_parsed = json.loads(bearer_token_response.text)
    return response_parsed["access_token"]


def set_bearer_token(bearer_token):
    headers["Authorization"] = "Bearer " + bearer_token

#retrieves last known value of each vehicle sensor obtained, with label, value and timestamp
def get_last_known_data(vin):
    last_known_data_response = requests.get(base_url + "/v1/" + vin + "/data/lastknown", headers=headers)
    return json.loads(last_known_data_response.text)

#retrieves all data collected from vehicle in past 24 hours
def get_twenty_four_hour_data(vin):
    twenty_four_hour_data_response = requests.get(base_url + "/v1/" + vin + "/data", headers=headers)
    return json.loads(twenty_four_hour_data_response.text)

#sends commands to vehicle
#available commands are  "LOCK, UNLOCK, START, STOP, HORNS"
def post_remote_command(vin, pin, command):
    remote_command_response = requests.post(base_url + "/v1/" + vin + "/remote", headers=headers,
                                            json={"command": command,
                                                  "pin": pin})
    return json.loads(remote_command_response.text)

def get_all_keys(d):
    for key, value in d.items():
        yield API_KEY
        if isinstance(value, dict):
            yield from get_all_keys(value)
    

def main():

    bearer_token = get_bearer_token()

    set_bearer_token(bearer_token)
   
    while True:
        print("-----------------")
        time.sleep(1.0 - ((time.time() - start_time) % 1.0))
        data = json.dumps(get_last_known_data(VEHICLE_VIN))
        data_2 = json.loads(data)


        for item in data_2["Items"]:
            vin = item["vin"]
            if (item["signal"] == "Speedometer"):
                speed = item["value"]
            
            if (item["signal"] == "Latitude"):
                latitude = item["value"]
            
            if (item["signal"] == "Longitude"):
                longitude = item["value"]

        x = requests.get("https://dev.virtualearth.net/REST/v1/Routes/SnapToRoad?points={},{}&includeTruckSpeedLimit=true&IncludeSpeedLimit=true&speedUnit=MPH&travelMode=driving&key=ApB3pE4UR5Px4wJangIVFcsZGmLzxlHvntQeam933MqxSW4aqIme9SaZO1T_XECy".format(latitude, longitude))
        y = x.json()


        for item in y["resourceSets"]:
            for r in item["resources"]:
                for z in r["snappedPoints"]:
                    speedLimit = z["speedLimit"]


        speedInformationDict = {
            "vin": vin,
            "speed": float(speed),
            "speedLimit": float(speedLimit),
        }
        speedInformation = json.dumps(speedInformationDict)

        print(speedInformation)

if __name__ == "__main__":
    main()
