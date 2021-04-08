def recursive_binary_search(list, target):
    """Returns True if the target value exists, else returns False

    Args:
        list ([type]): [description]
        target ([type]): [description]

    Returns:
        [type]: [description]
    """

    if len(list) == 0:
        # If the list is empty, it cannot contain the target
        return False
    else:
        midpoint = (len(list))//2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint+1:], target)
            else:
                return recursive_binary_search(list[:midpoint], target)

def verify(result):
    print("Target found:", result)

# This list must be sorted
numbers = [1,2,3,4,5,6,7,8,9,10]

result = recursive_binary_search(numbers, 12)
verify(result)

result = recursive_binary_search(numbers, 6)
verify(result)
