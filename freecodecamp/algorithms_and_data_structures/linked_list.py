class Node:
    """
    An object for storing a single node of a linked list.
    Models two attributes - data and the link to the next node in the list
    """

    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data

class LinkedList:
    """
    Singly linked list
    """

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        """Returns the number of nodes in the list
        Takes O(n) time ie: linear time

        Returns:
            [int]: The number of nodes in the list
        """
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node

        return count

    def add(self, data):
        """Add a new node to the beginning of the linked list

        Args:
            data ([type]): The data to be added to the linked list
        """

        new_node = Node(data)           # Create a new node from the data
        new_node.next_node = self.head  # Set the new node's next node value to the old head
        self.head = new_node            # Set the linked lists' head to the new node

    def search(self, key):
        """Search for the first node containing data that matches the key

        Takes O(n) time

        Args:
            key ([?]): The key to search for

        Returns:
            [Node]: The first node matching the key or None if not found
        """
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def __repr__(self):
        """Returns a string representation of the list
        Takes O(n) time
        """

        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node

        return '-> '.join(nodes)