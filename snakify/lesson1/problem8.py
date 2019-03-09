# https://snakify.org/en/lessons/print_input_numbers/problems/

# A timestamp is three numbers: a number of hours, minutes and seconds. Given two timestamps, calculate how many seconds is between them. The moment of the first timestamp occurred before the moment of the second timestamp.

print('First timestamp?')
hour1 = int(input('Hour: '))
minute1 = int(input('Minute: '))
second1 = int(input('Second: '))

print('Second timestamp?')
hour2 = int(input('Hour: '))
minute2 = int(input('Minute: '))
second2 = int(input('Second: '))

total_seconds1 = 60*60*hour1 + 60*minute1 + second1
total_seconds2 = 60*60*hour2 + 60*minute2 + second2

print(str(total_seconds2 - total_seconds1))
