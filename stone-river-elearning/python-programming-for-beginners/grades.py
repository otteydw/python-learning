#!/usr/bin/python3


def menu():
    print("""

    Welcome go Grade Central

    [1] - Enter Grades
    [2] - Remove Student
    [3] - Student Average Grades
    [4] - Exit

""")
    x = 0
    while x not in (1, 2, 3, 4):
        x = int(input("What would you like to do today? (Enter a number) "))
    return x


gradeDict = {}

while True:
    selection = menu()

    if selection == 1:
        # Enter Grades
        name = input('Student Name: ')
        grade = input('Grade: ')
        if name not in gradeDict:
            gradeDict[name] = []
        gradeDict[name].append(grade)
        print(gradeDict)
    elif selection == 2:
        # Remove Student
        name = input('Student Name: ')
        if name in gradeDict:
            del gradeDict[name]
        else:
            print('Student ' + name + ' does not exist.')
    elif selection == 3:
        # Student Average Grades
        print()
    elif selection == 4:
        # Exit
        exit()
