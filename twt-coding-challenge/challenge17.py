# Challenge 17: Back on time!
# You're on a 15 minute break at your TWT job. You decide to go on a 10 minute walk. The TWT office is in a city that is built based on a grid pattern. The city grid is such that no matter which block you choose it takes you 1 minute to walk through the block.
# ​
# Task
# Given a list containing the path chosen to walk in form of north, south, west and east directions, a single direction indicating walking a single block in that direction, determine whether or not you will return to the office with that path and if you'll make it in 10 minutes.

def solution(directions):

    if len(directions) > 10:
        return False

    starting_location = {'x': 0, 'y': 0}
    location = starting_location.copy()

    for direction in directions:
        if direction == 'n':
            location['y'] += 1
        elif direction == 's':
            location['y'] -= 1
        elif direction == 'w':
            location['x'] -= 1
        elif direction == 'e':
            location['x'] += 1

    return location == starting_location

# should be True
print(solution(['n', 'e', 's', 'w']))

# should be true
print(solution(['n', 'e', 's', 'w', 'n', 'e', 's', 'w']))

# should be False
print(solution(['e', 'n', 'n', 'w', 's']))

# should be false due to length?
print(solution(['n', 'e', 's', 'w', 'n', 'e', 's', 'w', 'n', 'e', 's', 'w']))

# should be true
print(solution(['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's']))