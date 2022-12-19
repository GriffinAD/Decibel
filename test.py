min_pwm_percent = 40
max_pwm_percent = 100
min_sensor_temp = 25
max_sensor_temp = 75


def CalcSpeed(temperature):
    if temperature <= min_sensor_temp:
        speedVal = min_pwm_percent
    elif temperature >= max_sensor_temp:
        speedVal = max_pwm_percent
    else:
        tPercent = ((temperature - min_sensor_temp)) / (max_sensor_temp - min_sensor_temp)
        speedVal = ((max_pwm_percent - min_pwm_percent) * tPercent) + min_pwm_percent
    # print(f"speed set: {speedVal} for temp: {temperature} C")
    return speedVal


for temp in range(min_sensor_temp - 5, max_sensor_temp + 5):
    speedVal = CalcSpeed(temp)
    print(f"speed set: {speedVal} for temp: {temp} C")
