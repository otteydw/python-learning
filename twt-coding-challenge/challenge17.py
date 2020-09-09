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