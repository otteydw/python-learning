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

    def insert(self, data, index):
        """Inserts a new node containing data at index position

        Insertion takes 0(1) time but finding the node at the insertion point
        takes 0(n) time.

        Takes overall 0(n) time

        Args:
            data (?): Data to insert
            index (int): Index position of insertion point
        """

        if index == 0:
            self.add(data)

        if index > 0:
            new_node = Node(data)

            position = index
            current = self.head

            while position > 1:
                current = self.next_node
                position -= 1

            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new_node
            new_node.next_node = next_node

    def remove_head(self):
        """Removes the head node
        """

        if not self.is_empty():
            original_head = self.head
            next_node = original_head.next_node
            self.head = next_node

    def remove(self, key):
        """Removes the first node containing the given key

        Args:
            key (?): The key to remove
        """

        current = self.head
        prev_node = None

        while current:
            if current.data == key:
                next_node = current.next_node
                if current == self.head:
                    self.remove_head()
                else:
                    prev_node.next_node = next_node
                return True

            prev_node = current
            current = current.next_node

        print('Key not found!')
        return False

    def remove_at_index(self, index):
        """Removes the node at the given index

        Args:
            index (int): The index of the node to delete
        """

        current = self.head
        prev_node = None
        position = 0

        while current:

            if position == index:
                next_node = current.next_node
                if current == self.head:
                    self.remove_head()
                else:
                    prev_node.next_node = next_node
                return True
            else:
                prev_node = current
                current = current.next_node
                position += 1

        print('Index not found!')
        return False

    def node_at_index(self, index):
        """Returns the node at the given index

        Args:
            index (int): The index of the node to delete

        Returns:
            Node: The node at the given index
        """

        current = self.head
        position = 0

        while current:

            if position == index:
                return current
            else:
                current = current.next_node
                position += 1

        print('Index not found!')
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

if __name__ == '__main__':
    # Create a sample linked list to experiment with
    l = LinkedList()
    l.add(5)
    l.add(4)
    l.add(6)
