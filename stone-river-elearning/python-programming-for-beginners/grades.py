#!/usr/bin/python3


class student:

    def __init__(self, name):
        self.name = name
        self.grades = []

    def addGrade(self, grade):
        self.grades.append(grade)

    def printGrades(self):
        print(self.grades)


student1 = student('Dan')

print(student1.name)
student1.addGrade(1)
student1.addGrade(10)
student1.printGrades()
