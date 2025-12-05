import sys
import csv

csv_reader = csv.reader(sys.stdin)
next(csv_reader)

for row in csv_reader:
    try:
        location_id, time, temp, humidity, dew, pressure, wind_speed, wind_dir, rain = row
        temp = float(temp)
        humidity = float(humidity)
        dew = float(dew)
        pressure = float(pressure)
        wind_speed = float(wind_speed)
        wind_dir = float(wind_dir)
        rain = float(rain)
        # Emit: city <tab> temp,humidity,dew, pressure, wind_speed, wind_dir, rain,1
        print(f"{location_id}\t{temp},{humidity},{dew},{pressure},{wind_speed},{wind_dir},{rain},1")

    except:
        continue