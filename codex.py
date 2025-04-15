import requests
import time
import serial

def sendData(value):
    ser.write(bytes(str(value), 'utf-8'))  # Send value as a byte

url = "https://api.thingspeak.com/channels/2920014/fields/1.json?api_key=X6IMS820SQ2E9N3E&results=1"
lastvalue = -1
ser = serial.Serial('COM7', 9600, timeout=1)

while True:
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        feeds = data.get("feeds", [])
        
        if feeds:
            value = feeds[0].get("field1")
            print("Latest field1 value:", value)
            
            if value != lastvalue:
                print("Toggled")
                lastvalue = value
                sendData(value)  # Corrected indentation here
        else:
            print("No data found in feeds.")
    else:
        print("Failed to fetch data. Status code:", response.status_code)
