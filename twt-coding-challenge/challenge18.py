# Challenge 18: Apple Boxes!
# You have k apple boxes full of apples. Each square box of size m contains m × m apples. You just noticed two interesting properties about the boxes:

# 1.--The smallest box is size 1, the next one is size 2,..., all the way up to size k.

# 2.--Boxes that have an odd size contain only yellow apples. Boxes that have an even size contain only red apples.
# ‍
# Task:
# Your task is to calculate the difference between the number of red apples and the number of yellow apples.

def solution(k):

    numYellow = numRed = 0

    for i in range(1, k+1):
        applesInBox = i*i
        if (i % 2) == 0:
            numRed += applesInBox
        else:
            numYellow += applesInBox

    return numRed - numYellow

print(solution(1))
print()
# Should return -15
print(solution(5))

print()

print(solution(101))