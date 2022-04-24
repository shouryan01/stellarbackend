import json
from score import get_score
import requests

def read_file():
    with open('hackathondata_testdrive.txt') as f:
        lines = f.readlines()

def boolScoreSum(ABSIndLampStatus, AutomaticOilChange, Door_Ajar_Status, DriverBelt, LowWasherFluid, MaintenanceReminderStatus, OilLifeSts):

    return ABSIndLampStatus + AutomaticOilChange + Door_Ajar_Status + DriverBelt + LowWasherFluid + MaintenanceReminderStatus + OilLifeSts   


def calculateScore(speed, speedLimit, boolScoreSum, EngineRPM, ABSIndLampStatus, AutomaticOilChange, Door_Ajar_Status, DriverBelt, LowWasherFluid, MaintenanceReminderStatus, OilLifeSts):
    points = 0
    if (speed >speedLimit-17 and speed<speedLimit+5):
        points=points+10
    
    #add up all the values from abs ind lamp to oil life and call it boolScoreSum
    boolScore=boolScoreSum(ABSIndLampStatus, AutomaticOilChange, Door_Ajar_Status, DriverBelt, LowWasherFluid, MaintenanceReminderStatus, OilLifeSts)

    if(boolScore==0):
        points=points+4
    elif (boolScore >0 and boolScoreSum < 3):
        points=points-2
    elif (boolScoreSum == 7):
        points=points-15

    if (EngineRPM > 1500 and EngineRPM < 3000):
        points=points+1
    else: 
        points=points-2

    return(points)



def main():
    
    f = open("scoreData.txt", "a")
    while True:
        f.write(json.dumps(calculateScore))
        f.write("\n \n")

if __name__ == "_main_":
    main()