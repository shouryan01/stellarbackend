import time
import json, requests



start_time = time.time()
# seconds = 4


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
        print("tick")
        time.sleep(1.0 - ((time.time() - start_time) % 1.0))
        data = json.dumps(get_last_known_data(VEHICLE_VIN))
        data_2 = json.loads(data)

        for item in data_2["Items"]:
            # print(item)
            # print(item["signal"])
            # print(item["value"])
            # print(type(item))
            length = len(data_2)
            i=0
            # while i < length:
            if (item["signal"] == "Speedometer"):
                print(item["value"])
            
            if (item["signal"] == "Latitude"):
                print(item["value"])
            
            if (item["signal"] == "Longitude"):
                print(item["value"])


                # i += 1
                    # break


    

    # print(get_last_known_data(VEHICLE_VIN))

    # data = json.loads(get_last_known_data(VEHICLE_VIN))
    

    # for x in get_all_keys(data_2):
    #     print(x)

    # print(get_twenty_four_hour_data(VEHICLE_VIN))

    # print(type(data_2))

    # print(post_remote_command(VEHICLE_VIN, VEHICLE_PIN, "LOCK"))

if __name__ == "__main__":
    main()

