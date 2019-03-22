# https://snakify.org/en/lessons/if_then_else_conditions/problems/

# For the given integer X print 1 if it's positive, -1 if it's negative, or 0 if it's equal to zero.
# Try to use the cascade if-elif-else for it.

x = int(input('Integer: '))

if x < 0:
    print('-1')
elif x > 0:
    print('1')
else:
    print('0')
