from linked_list import LinkedList

def merge_sort(linked_list):

    if linked_list.size() <= 1:
        # print(linked_list)
        return linked_list

    left_half, right_half = split(linked_list)
    # print('L Half:', left_half)
    # print('R Half:', right_half)
    left_list = merge_sort(left_half)
    right_list = merge_sort(right_half)

    return merge(left_list, right_list)

def split(linked_list):
    # print('List size: ', linked_list.size())
    mid = linked_list.size()//2
    # print('Mid: ', mid)

    left_list = LinkedList()
    right_list = LinkedList()

    for x in range(linked_list.size()):
        # print('Step: ', x)
        if x < mid:
            # print('Left path')
            left_list.add(linked_list.node_at_index(x).data)
        else:
            # print('Right path')
            right_list.add(linked_list.node_at_index(x).data)

    return left_list, right_list

def merge(left_list, right_list):
    new_list = LinkedList()
    left_index = 0
    right_index = 0
    # print('L list size: ', left_list.size())
    # print('R list size: ', right_list.size())

    # Loop through both lists. Append the higher element into the new list and then increment that list's index
    while left_index < left_list.size() and right_index < right_list.size():
        left_data = left_list.node_at_index(left_index).data
        right_data = right_list.node_at_index(right_index).data
        # print('L Data: ', left_data)
        # print('R Data: ', right_data)
        if left_data < right_data:
            new_list.add(left_data)
            # new_list.insert(left_data, new_list.size()-1)
            left_index += 1
        else:
            new_list.add(right_data)
            # new_list.insert(right_data, new_list.size()-1)
            right_index += 1
        # print('New List: ', new_list)

    # If the left list is larger than the right, just append each remaining element from the left list
    while left_index < left_list.size():
        # print('L index:', left_index)
        new_list.add(left_data)
        # new_list.insert(left_data, new_list.size())
        left_index += 1

    # If the right list is larger than the left, just append each remaining element from the right list
    while right_index < right_list.size():
        # print('R index:', right_index)
        new_list.add(right_data)
        # new_list.insert(right_data, new_list.size())
        right_index += 1

    return new_list

if __name__ == '__main__':
    # Create a sample linked list to experiment with
    l = LinkedList()
    l.add(5)
    l.add(4)
    l.add(6)
    l.add(7)
    l.add(3)
    l.add(4)
    l.add(2)

    # left, right = split(l)

    s1 = LinkedList()
    s1.add(1)

    s2 = LinkedList()
    s2.add(2)

    d = LinkedList()
    d.add(2)
    d.add(1)

    drev = LinkedList()
    drev.add(1)
    drev.add(2)

    trip = LinkedList()
    trip.add(1)
    trip.add(2)
    trip.add(3)