# https://snakify.org/en/lessons/integer_float_numbers/problems/

# H hours, M minutes and S seconds are passed since the midnight(0 ≤ H < 12, 0 ≤ M < 60, 0 ≤ S < 60). Determine the angle(in degrees) of the hour hand on the clock face right now.

# Number of seconds in 12 hour period
seconds_per_clock = 43200

hours = int(input('Hours: '))
minutes = int(input('Minutes: '))
seconds = int(input('Seconds: '))
total_seconds = (3600 * hours) + (60 * minutes) + seconds

# If the total_seconds is more than half a day, the clock has wrapped around
clock_seconds = int(total_seconds % (seconds_per_clock))

# percentage around the clock
clock_percentage = float(clock_seconds) / float(seconds_per_clock)

# convery the percentage into degrees of a circle
clock_degrees = round((360 * clock_percentage), 8)

print(clock_degrees)
