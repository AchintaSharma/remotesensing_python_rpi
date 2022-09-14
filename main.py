import sys
from imageCam import runCamera
from tempSensor import runTempSensor

def loadSensorDriver():
    import loadsensor
    input("\nPlace weight and press enter to start reading...")
    print("Reading weight. Please wait...")
    weight = loadsensor.runLoadSensor()
    print(int(weight));

def tempSensorDriver():
    tempC = round(runTempSensor(), 1)
    tempF = (tempC * 9.0/5.0) + 32.0
    print(f"\nObject Temp. : {tempC}°C ({tempF}°F)")

while True:
    print("\n\n")
    print("Welcome to remote sensing!") 
    print("1. Measure weight")
    print("2. Measure temperature")
    print("3. Click Photo")
    print("4. Combined report (Weight, Temp and Image)")
    print("5. Stream Live")
    print("6. Exit")

    choice = input("\n\nEnter choice: ")

    if(choice == "1"):
        loadSensorDriver()

    elif(choice == "2"):
        tempSensorDriver()

    elif(choice == "3"):
        runCamera()
        
    elif(choice == "4"):
       loadSensorDriver()
       tempSensorDriver()
       runCamera()


    elif(choice == "6"):
        sys.exit()
