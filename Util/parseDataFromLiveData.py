import time
import json, requests


start_time = time.time()
# pasted API keys here
API_KEY = "fvm1e2NVAk1Ayvm58NYxS8IHtvRHPC2N4sWtOsjz"
API_USERNAME = "alex.burke@fcagroup.com"
API_PASSWORD = "Hackathon1!"
VEHICLE_VIN = "1C4RJFBGXMC877858"
VEHICLE_PIN = 1234

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
    f = open("speedLimitData.txt", "a")
    while True:
        print("-----------------")
        time.sleep(1.0 - ((time.time() - start_time) % 1.0))
        data = json.dumps(get_last_known_data(VEHICLE_VIN))
        data_2 = json.loads(data)

        for item in data_2["Items"]:
            vin = item["vin"]
            if (item["signal"] == "VehSpdDisp"):
                speed = item["value"]
            elif (item["signal"] == "Latitude"):
                latitude = item["value"]
            elif (item["signal"] == "Longitude"):
                longitude = item["value"]
            elif (item["signal"] == "ABSIndLampStatus"):
                ABSIndLampStatus = item["value"]
            elif (item["signal"] == "AutomaticOilChange"):
                AutomaticOilChange = item["value"]
            elif (item["signal"] == "Door_Ajar_Status"):
                Door_Ajar_Status = item["value"]
            elif (item["signal"] == "DriverBelt"):
                DriverBelt = item["value"]
            elif (item["signal"] == "FuelLvlLow"):
                FuelLvlLow = item["value"]
            elif (item["signal"] == "LowWasherFluid"):
                LowWasherFluid = item["value"]
            elif (item["signal"] == "MaintenanceReminderStatus"):
                MaintenanceReminderStatus = item["value"]
            elif (item["signal"] == "OilLifeSts"):
                OilLifeSts = item["value"]
            elif (item["signal"] == "PresentGear"):
                PresentGear = item["value"]
            elif (item["signal"] == "TransOverTemp"):
                TransOverTemp = item["value"]
            elif (item["signal"] == "AvgFuelEcon"):
                AvgFuelEcon = item["value"]
            elif (item["signal"] == "EngineRPM"):
                EngineRPM = item["value"]
            elif (item["signal"] == "TirePressFL"):
                TirePressFL = item["value"]
            elif (item["signal"] == "TirePressFR"):
                TirePressFR = item["value"]
            elif (item["signal"] == "TirePressRL"):
                TirePressRL = item["value"]
            elif (item["signal"] == "TirePressRR"):
                TirePressRR = item["value"]
            elif (item["signal"] == "Altitude"):
                Altitude = item["value"]
            elif (item["signal"] == "ATMPressure"):
                ATMPressure = item["value"]
            elif (item["signal"] == "AverageTemp"):
                AverageTemp = item["value"]
            elif (item["signal"] == "Odometer"):
                Odometer = item["value"]
            elif (item["signal"] == "EngineCoolant"):
                EngineCoolant = item["value"]
            elif (item["signal"] == "EngineOilTemp"):
                EngineOilTemp = item["value"]
            elif (item["signal"] == "SteeringWheelAngle"):
                SteeringWheelAngle = item["value"]
            elif (item["signal"] == "ExteriorTemperature"):
                ExteriorTemperature = item["value"]
            elif (item["signal"] == "AverageTemp"):
                AverageTemp = item["value"]
            elif (item["signal"] == "TargetGear"):
                TargetGear = item["value"]
            elif (item["signal"] == "TurnInd_LT_ON"):
                TurnInd_LT_ON = item["value"]
            elif (item["signal"] == "TurnInd_RT_ON"):
                TurnInd_RT_ON = item["value"]

        x = requests.get("https://dev.virtualearth.net/REST/v1/Routes/SnapToRoad?points={},{}&includeTruckSpeedLimit=true&IncludeSpeedLimit=true&speedUnit=MPH&travelMode=driving&key=ApB3pE4UR5Px4wJangIVFcsZGmLzxlHvntQeam933MqxSW4aqIme9SaZO1T_XECy".format(latitude, longitude))
        y = x.json()


        for item in y["resourceSets"]:
            for r in item["resources"]:
                for z in r["snappedPoints"]:
                    speedLimit = z["speedLimit"]


        speedInformationDict = {
            "vin": vin,
            "speed": float(speed),
            "speedLimit": float(speedLimit) * 1.609344,
            "ABSIndLampStatus": ABSIndLampStatus,
            "AutomaticOilChange": AutomaticOilChange,
            "Door_Ajar_Status": Door_Ajar_Status,
            "DriverBelt": DriverBelt,
            "FuelLvlLow": FuelLvlLow,
            "LowWasherFluid": LowWasherFluid,
            "MaintenanceReminderStatus": MaintenanceReminderStatus,
            "OilLifeSts": OilLifeSts,
            "PresentGear": PresentGear,
            "TransOverTemp": TransOverTemp,
            "AvgFuelEcon": AvgFuelEcon,
            "EngineRPM": EngineRPM,
            "TirePressFL": TirePressFL,
            "TirePressFR": TirePressFR,
            "TirePressRL": TirePressRL,
            "TirePressRR": TirePressRR,
            "Altitude": Altitude,
            "ATMPressure": ATMPressure,
            "AverageTemp": AverageTemp,
            "Odometer": Odometer,
            "latitude": latitude,
            "longitude": longitude,
            "EngineCoolant": EngineCoolant,
            "EngineOilTemp": EngineOilTemp,
            "SteeringWheelAngle": SteeringWheelAngle,
            "ExteriorTemperature": ExteriorTemperature,
            "AverageTemp": AverageTemp,
            "TargetGear": TargetGear,
            "TurnInd_LT_ON": TurnInd_LT_ON,
            "TurnInd_RT_ON": TurnInd_RT_ON,
        }

        speedInformation = json.dumps(speedInformationDict)
        f.write(speedInformation)
        f.write("\n")
        print(speedInformation)

        requests.post("http://localhost:8000/api/data/", data=speedInformation)

if __name__ == "__main__":
    main()
