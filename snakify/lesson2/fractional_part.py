# https://snakify.org/en/lessons/integer_float_numbers/problems/

# Given a positive real number, print its fractional part.

import math

a = float(input('Enter a postitive real number: '))

fractional_length = len(str(a).split('.')[1])
fractional_part = a - math.floor(a)
result = round(fractional_part, fractional_length)

print(result)
