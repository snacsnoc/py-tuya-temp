#!/usr/bin/python3
import os
import subprocess
import sys
from flask import Flask, render_template
import tinytuya

app = Flask(__name__)

tuya_ip = os.getenv('TUYA_IP')
tuya_device_id = os.getenv('TUYA_DEVICE')
tuya_key = os.getenv('TUYA_KEY')

# Check our Tuya device is online
ping_output = subprocess.run(
    ["ping", "-c", "1", "-W", "1", tuya_ip], capture_output=True
)

if ping_output.returncode == 0:
    print("Device is reachable")
else:
    print("Device is not reachable")
    sys.exit()

d = tinytuya.OutletDevice(
    dev_id=tuya_device_id,
    address=tuya_ip,
    local_key=tuya_key,
    version=3.4,
)

# Get Status
dps = d.detect_available_dps()


temperature = str(dps["1"])
if temperature[0] == "-":
    temperature = "-" + temperature[1] + "." + temperature[2:]
else:
    temperature = temperature[:2] + "." + temperature[2:]

humidity = str(dps["2"])
if len(humidity) == 3:
    humidity = humidity[:2] + "." + humidity[2:]
else:
    humidity = humidity[:1] + "." + humidity[1:]

data = {"temperature": temperature, "humidity": humidity, "lux": dps["16"], "dps": dps}


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", data=data)


if __name__ == "__main__":
    app.run()
