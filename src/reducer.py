import sys

current_location = None
sum_temp = 0
sum_humidity = 0 
sum_dew = 0 
sum_pressure = 0
sum_wind_speed = 0
sum_wind_dir = 0 
sum_rain = 0
max_temp = float("-inf")
min_temp = float("inf")
count = 0

for line in sys.stdin:

    line = line.strip()
    if not line:
        continue

    location, values = line.split("\t")
    temp, humidity, dew, pressure, wind_speed, wind_dir, rain ,one = values.split(",")

    temp = float(temp)
    humidity = float(humidity)
    dew = float(dew)
    pressure = float(pressure)
    wind_speed = float(wind_speed)
    wind_dir = float(wind_dir)
    rain = float(rain)
    one = int(one)

    if location == current_location:
        sum_temp += temp
        sum_humidity += humidity
        sum_dew += dew
        sum_pressure += pressure
        sum_wind_speed += wind_speed
        sum_wind_dir += wind_dir
        sum_rain += rain
        count += one
        max_temp = max(max_temp,temp)
        min_temp = min(min_temp,temp)

    else:

        if current_location:
            avg_temp = sum_temp / count
            avg_humidity = sum_humidity / count
            avg_dew = sum_dew / count
            avg_pressure = sum_pressure / count
            avg_windspeed = sum_wind_speed / count
            avg_wind_dir = sum_wind_dir / count
            avg_rain = sum_rain / count

            print(f"Location:{current_location}\tAvg Temp:{avg_temp:.2f}, Avg Humidity:{avg_humidity:.2f}, Avg Dew:{avg_dew:.2f}, Avg Pressure:{avg_pressure:.2f}, Avg Windspeed:{avg_windspeed:.2f}, Avg Wind Direction:{avg_wind_dir:.2f}, Avg Rain amount:{avg_rain:.2f}")

        current_location = location
        sum_temp = temp
        sum_humidity = humidity
        sum_dew = dew
        sum_pressure = pressure
        sum_wind_speed = wind_speed
        sum_wind_dir = wind_dir
        sum_rain = rain
        count = one
        max_temp = temp
        min_temp =temp

if current_location:
        
    avg_temp = sum_temp / count
    avg_humidity = sum_humidity / count
    avg_dew = sum_dew / count
    avg_pressure = sum_pressure / count
    avg_windspeed = sum_wind_speed / count
    avg_wind_dir = sum_wind_dir / count
    avg_rain = sum_rain / count

    print(f"Location:{current_location}\tAvg Temp:{avg_temp:.2f}, Avg Humidity:{avg_humidity:.2f}, Avg Dew:{avg_dew:.2f}, Avg Pressure:{avg_pressure:.2f}, Avg Windspeed:{avg_windspeed:.2f}, Avg Wind Direction:{avg_wind_dir:.2f}, Avg Rain amount:{avg_rain:.2f}")