import sensor

sensorPattern = "Source: {} - Value: {}"

sensorData = sensor.read_sensor()

print(sensorPattern.format(sensorData["Source"], sensorData["Value"]))