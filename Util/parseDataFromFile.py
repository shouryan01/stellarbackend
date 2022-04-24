import json
import os
import requests
from pprint import pprint
def getDataListItems(list):
    print(list)
    print(type(list))

def main():

    with open(os.getcwd() + '/hackathondata_testdrive.txt') as f:
        lines = [line for line in f.readlines() if line.strip()]

    print("-----------------")
    for line in lines:
        line2 = json.loads(line)
        for item in line2["Items"]:
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
            "speedlimit": float(speedLimit) * 1.609344,
            "ABSIndLampStatus": int(ABSIndLampStatus),
            "AutomaticOilChange": int(AutomaticOilChange),
            "Door_Ajar_Status": int(Door_Ajar_Status),
            "DriverBelt": int(DriverBelt),
            "FuelLvlLow": int(FuelLvlLow),
            "LowWasherFluid": int(LowWasherFluid),
            "MaintenanceReminderStatus": int(MaintenanceReminderStatus),
            "OilLifeSts": int(OilLifeSts),
            "PresentGear": int(PresentGear),
            "TransOverTemp": int(TransOverTemp),
            "AvgFuelEcon": AvgFuelEcon,
            "EngineRPM": int(EngineRPM),
            "TirePressFL": int(TirePressFL),
            "TirePressFR": int(TirePressFR),
            "TirePressRL": int(TirePressRL),
            "TirePressRR": int(TirePressRR),
            "Altitude": float(Altitude),
            "ATMPressure": int(ATMPressure),
            "AverageTemp": int(AverageTemp),
            "Odometer": float(Odometer),
            "latitude": float(latitude),
            "longitude": float(longitude),
            "EngineCoolant": int(EngineCoolant),
            "EngineOilTemp": int(EngineOilTemp),
            "SteeringWheelAngle": float(SteeringWheelAngle),
            "ExteriorTemperature": float(ExteriorTemperature),
            "AverageTemp": int(AverageTemp),
            "TargetGear": int(TargetGear),
            "TurnInd_LT_ON": int(TurnInd_LT_ON),
            "TurnInd_RT_ON": int(TurnInd_RT_ON),
        }

        speedInformation = json.dumps(speedInformationDict)
        # print(type(speedInformationDict["Altitude"]))
        x = requests.post("http://localhost:8000/api/data/", data=speedInformationDict)
        


if __name__ == "__main__":
    main()