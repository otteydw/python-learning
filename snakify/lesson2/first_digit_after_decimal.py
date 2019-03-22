# https://snakify.org/en/lessons/integer_float_numbers/problems/

# Given a positive real number, print its first digit to the right of the decimal point.

a = float(input('Enter a postitive real number: '))

fractional_part = str(a).split('.')[1]
result = fractional_part[0]

print(result)
