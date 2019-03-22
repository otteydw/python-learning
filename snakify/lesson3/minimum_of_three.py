# https://snakify.org/en/lessons/if_then_else_conditions/problems/

# Given three integers, print the smallest value.

a = int(input('Integer 1: '))
b = int(input('Integer 2: '))
c = int(input('Integer 3: '))

if a <= b and a <= c:
    print(a)
elif b <= a and b <= c:
    print(b)
else:
    print(c)
