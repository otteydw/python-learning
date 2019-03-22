# https://snakify.org/en/lessons/integer_float_numbers/problems/

# A cupcake costs A dollars and B cents. Determine, how many dollars and cents should one pay for N cupcakes. A program gets three numbers: A, B, N. It should print two numbers: total cost in dollars and cents.

a = int(input('Dollars: '))
b = int(input('Cents: '))
n = int(input('Quantity: '))

total_cost = n * (a + float(b)/100)

dollars = str(total_cost).split('.')[0]
cents = str(total_cost).split('.')[1]

print(str(dollars) + ' ' + str(cents))
