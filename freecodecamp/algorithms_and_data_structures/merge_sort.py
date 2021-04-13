def merge_sort(list):
    """Sorts a list in ascending order

    Divide: Find the midpoint of the list and divide into sublists
    Conquer: Recursively sort the sublists from the previous step
    Combine: Merge the sorted sublists created in the previous step

    Args:
        list ([type]): [description]

    Returns:
        [type]: A new sorted list
    """

    # The stopping condition is when the list is as small as possible.
    # This list is therefore naively sorted
    if len(list) <= 1:
        return list

    left_half, right_half = split(list)

    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(mylist):
    """Divide the unsorted list at midpoint into sublists

    Args:
        list (list): The list to be split

    Returns:
        left, right: Unsorted lists
    """

    mid = len(mylist)//2

    left = mylist[:mid]
    right = mylist[mid:]

    return left, right

def merge(left, right):
    """Merges two lists, sorting them in the process

    Args:
        list1 ([type]): [description]
        list2 ([type]): [description]

    Returns:
        [type]: A new list
    """

    new_list = []
    left_index = 0
    right_index = 0

    # Loop through both lists. Append the higher element into the new list and then increment that list's index
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            new_list.append(left[left_index])
            left_index += 1
        else:
            new_list.append(right[right_index])
            right_index += 1

    # If the left list is larger than the right, just append each remaining element from the left list
    while left_index < len(left):
        new_list.append(left[left_index])
        left_index += 1

    # If the right list is larger than the left, just append each remaining element from the right list
    while right_index < len(right):
        new_list.append(right[right_index])
        right_index += 1

    return new_list

def verify_sorted(mylist):
    """Determine if a list is sorted

    Args:
        mylist (array): A list to check for sortedness.

    Returns:
        boolean: True if the list is sorted. Otherwise false.
    """

    for index, value in enumerate(mylist):
        if index < len(mylist) - 1 and value > mylist[index + 1]:
            return False
    return True

if __name__ == '__main__':

    alist = [100, 27, 53, 29, 68, 12, 9, 0]

    print(verify_sorted(alist))

    l = merge_sort(alist)

    print(l)

    print(verify_sorted(l))

    empty_list = []
    print(verify_sorted(empty_list))

    one_element = [7]
    print(verify_sorted(one_element))