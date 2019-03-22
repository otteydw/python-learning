# https://snakify.org/en/lessons/integer_float_numbers/problems/

# A car can cover distance of N kilometers per day. How many days will it take to cover a route of length M kilometers? The program gets two numbers: N and M.

import math

n = int(input('Number of kilometers per day: '))
m = int(input('Route length in kilometers: '))

result = math.ceil(m / n)

print(result)
