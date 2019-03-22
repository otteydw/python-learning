# https://snakify.org/en/lessons/integer_float_numbers/problems/

# Hour hand turned by α degrees since the midnight. Determine the angle by which minute hand turned since the start of the current hour. Input and output in this problems are floating-point numbers.

# Number of degrees the hour hand turns per hour
hour_hand_degrees_per_hour = 30
minute_hand_degrees_per_hour = 360

# Total number of degrees the hour hand has turned
hour_hand_degrees = float(input('Degrees: '))

# The number of degrees the hour hand has turned during the current hour
current_hour_hour_hand_degrees = hour_hand_degrees % hour_hand_degrees_per_hour

result = int(360 * current_hour_hour_hand_degrees / hour_hand_degrees_per_hour)

print(str(result))
