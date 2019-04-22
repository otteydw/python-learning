#!/usr/bin/python3


class student:

    def __init__(self, name):
        self.name = name
        self.grades = []

    def addGrade(self, grade):
        self.grades.append(grade)

    def printGrades(self):
        print(self.grades)


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


while True:
    selection = menu()

    if selection == 1:
        # Enter Grades
        print()
    elif selection == 2:
        # Remove Student
        print()
    elif selection == 3:
        # Student Average Grades
        print()
    elif selection == 4:
        # Exit
        exit()
