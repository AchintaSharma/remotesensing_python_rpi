import sys
from imageCam import runCamera
from tempSensor import runTempSensor
from humidityTemp import runHumiTempSensor

def loadSensorDriver():
    import loadsensor
    input("\nPlace weight and press enter to start reading...")
    print("Reading weight. Please wait...")
    weight = loadsensor.runLoadSensor()
    print("Weight: "+str(round(float(weight/1000),3))+" kg");
    return weight

def tempSensorDriver():
    tempC = round(runTempSensor(), 1)
    tempF = (tempC * 9.0/5.0) + 32.0
    print(f"\nObject Temp.: {tempC}°C ({tempF}°F)")
    return [tempF, tempC]

def humidityTempSensorDriver():
    temp = runHumiTempSensor()[0]
    humidity = runHumiTempSensor()[1]
    print("Temperature: {}*C   Humidity: {}% ".format(temp, humidity))
    return [temp, humidity]

def main():
    while True: 
        choice = input("\n\nDo you want to read data? (Y/N): ")
        
        if(choice == "Y" or choice == "y"):
            temperature = tempSensorDriver()
            weight = loadSensorDriver();
            ambienttemp = humidityTempSensorDriver()[0];
            return {
                "temperature": str(temperature[1])+"°C ("+str(temperature[0])+" °F)",
                "weight": str(round(weight/1000,3))+"kg",
                "ambienttemp": str(ambienttemp)+"°C" 
            }
        else: 
            sys.exit() 


# def main():
#     while True:
#         print("\n\n")
#         print("Welcome to remote sensing!") 
#         print("1. Measure weight")
#         print("2. Measure temperature")
#         print("3. Click Photo")
#         print("4. Combined report (Weight, Temp and Image)")
#         print("5. Stream Live")
#         print("6. Exit")

#         choice = input("\n\nEnter choice: ")

#         if(choice == "1"):
#             weight = loadSensorDriver()
#             return weight;

#         elif(choice == "2"):
#             tempSensorDriver()

#         elif(choice == "3"):
#             file = runCamera()
#             return file;
            
#         elif(choice == "4"):
#             loadSensorDriver()
#             tempSensorDriver()
#             runCamera()


#         elif(choice == "6"):
#             sys.exit()
