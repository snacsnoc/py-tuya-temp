# Tuya Temperature Monitor
Post: https://geekness.eu/python-tinytuya-temperature-monitor

Simple Flask app to connect to your Tuya Temperature monitor

![screenshot](https://github.com/snacsnoc/py-tuya-temp/blob/main/static/img/screenshot.png?raw=true)

Requirements:
```bash
pip install tinytuya flask
```
Environment variables:
```bash
TUYA_IP
TUYA_KEY
TUYA_DEVICE
```
You can get a key by creating a [Tuya Developer account](https://iot.tuya.com/), see post at top of readme.

Run:
```bash
python3 app.py
```
## DPS lookup table for Tuya Temperature Monitor

Note: For all temperatures, pad a decimal from the right. 452=45.2

| DPS | Value | Description | Unit | Info |
| --- | --- | --- | --- | --- |
| 1   | 60  | Temperature | integer |     |
| 2   | 452 | Humidity (%) | integer |     |
| 4   | 100 | Battery | integer | 3.7V/500mAh, Built-in battery usage time: ≤4 hours (fully charged) |
| 9   | c   | Temperature unit | c/f |     |
| 10  | 1500 | Alarm Temperature upper limit | integer | Temperature alarm setting |
| 11  | -190 | Alarm Temperature lower limit | integer | Temperature alarm setting |
| 12  | 1000 | Humidity upper limit | integer | Humidity alarm setting |
| 13  | 244 | Humidity lower limit (24.4%) | integer | Humidity alarm setting |
| 14  | cancel | Temperature Alarm | on/cancel |     |
| 15  | cancel | Humidity Alarm | on/cancel |     |
| 16  | 0   | Light intensity | integer | Lux |
| 17  | 30  | Temperature report | integer | Alarm duration in seconds |
| 18  | 30  | Humidity report | integer | Alarm duration in seconds |
| 21  | true | Battery Switch | true/false | Enable battery backup |
| 23  | 0   | Temperature calibration | C +/- | Manually set positive or negative offset |
| 24  | 0   | Humidity Calibration | C +/- | Manually set positive or negative offset |