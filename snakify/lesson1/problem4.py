# https://snakify.org/en/lessons/print_input_numbers/problems/

# Write a program that reads the length of the base and the height of a right-angled triangle and prints the area. Every number is given on a separate line.

length = int(input('Length: '))
height = int(input('Height: '))

area = (length * height)/2

print('The area is ' + str(area))
