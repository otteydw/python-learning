import sys

x = y = 0
for movement in sys.argv[1]:
    if movement == 'U':
        y += 1
    elif movement == 'D':
        y -= 1
    elif movement == 'L':
        x -= 1
    elif movement == 'R':
        x += 1

print(f"{x},{y}")