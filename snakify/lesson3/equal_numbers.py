# https://snakify.org/en/lessons/if_then_else_conditions/problems/

# Given three integers, determine how many of them are equal to each other.
# The program must print one of these numbers: 3 (if all are the same), 2 (if two of them are equal to each other and the third is different) or 0 (if all numbers are different).

a = int(input('Integer 1: '))
b = int(input('Integer 2: '))
c = int(input('Integer 3: '))

if a == b and a == c:
    print('3')
elif a == b or b == c or a == c:
    print('2')
else:
    print('0')
