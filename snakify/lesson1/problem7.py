# https://snakify.org/en/lessons/print_input_numbers/problems/

# Write a program that reads an integer number and prints its previous and next numbers. See the examples below for the exact format your answers should take. There shouldn't be a space before the period.
# Remember that you can convert the numbers to strings using the function str.

number = int(input('Enter an integer: '))

print('The previous number is ' + str(number - 1) + '.')
print('The next number is ' + str(number + 1) + '.')
