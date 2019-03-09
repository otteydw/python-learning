# https://snakify.org/en/lessons/print_input_numbers/problems/

# N students take K apples and distribute them among each other evenly. The remaining(the undivisible) part remains in the basket. How many apples will each single student get? How many apples will remain in the basket?
# The program reads the numbers N and K. It should print the two answers for the questions above.

n = int(input('Number of students: '))
k = int(input('Number of apples: '))

print('Apples per student: ' + str(k//n))
print('Apples in basket: ' + str(k % n))
