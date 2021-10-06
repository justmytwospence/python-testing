import doctest


class Node:
    """
    A class to represent a doubly-linked node.
    """

    def __init__(self, value, next=None, previous=None):
        """
        >>> node = Node(1)
        >>> node
        None -> 1 -> None
        >>> node.previous = Node(0)
        >>> node.next = Node(2)
        >>> node
        0 -> 1 -> 2
        """
        self.value = value
        self.next = next
        self.previous = previous

    def __repr__(self):
        previous_value = self.previous.value if self.previous else None
        next_value = self.next.value if self.next else None
        return " -> ".join(map(str, [previous_value, self.value, next_value]))


class LinkedList:
    """
    A class to represent a doubly-linked list.
    """

    def __init__(self, nodes):
        """
        Initialize a doubly linked list from a list of nodes.
        :param: nodes: list
        >>> ll = LinkedList([1,2,3,4])
        >>> ll.head
        None -> 1 -> 2
        >>> ll.tail
        3 -> 4 -> None
        """
        self.head = Node(nodes.pop(0))
        current_node = self.head
        for new_node in nodes:
            new_node = Node(new_node, previous=current_node)
            current_node.next = new_node
            current_node = current_node.next
        self.tail = current_node

    def __iter__(self):
        """
        >>> ll = LinkedList([1,2,3])
        >>> for node in ll:
        ...     print(node)
        None -> 1 -> 2
        1 -> 2 -> 3
        2 -> 3 -> None
        """
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next

    def __repr__(self):
        """
        Visualize doubly linked list.
        >>> LinkedList([1,2,3,4])
        1 -> 2 -> 3 -> 4 -> None
        """
        current_node = self.head
        node_values = []
        while current_node:
            node_values.append(current_node.value)
            current_node = current_node.next
        node_values.append(None)
        return " -> ".join([str(x) for x in node_values])

    def add_first(self, value):
        """
        Insert node at head.
        >>> ll = LinkedList([1,2,3,4])
        >>> ll.add_first(0)
        0 -> 1 -> 2 -> 3 -> 4 -> None
        """
        new_node = Node(value, next=self.head)
        self.head = new_node
        return self

    def add_last(self, value):
        """
        Insert node at tail.
        >>> ll = LinkedList([1,2,3,4])
        >>> ll.add_last(5)
        1 -> 2 -> 3 -> 4 -> 5 -> None
        """
        new_node = Node(value, previous=self.tail)
        self.tail.next = new_node
        self.tail = new_node
        return self

    def insert_position(self, value, position):
        """
        Insert node at position
        >>> ll = LinkedList([1,2,3,4])
        >>> ll.insert_position(5, 2)
        1 -> 2 -> 5 -> 3 -> 4 -> None
        >>> ll.insert_position(6, 20)
        Traceback (most recent call last):
        Exception: Position not in list
        """
        if position == 0:
            self.add_first(value)
        else:
            current_node = self.head
            idx = 0
            while current_node and idx < position:
                idx += 1
                current_node = current_node.next
            if current_node:
                new_node = Node(
                    value, previous=current_node.previous, next=current_node)
                current_node.previous.next = new_node
                current_node.previous = new_node
            else:
                raise Exception("Position not in list")
        return self

    def insert_after(self, value, target):
        """
        Insert node just after first instance of target
        >>> ll = LinkedList([1,2,3,4,5])
        >>> ll.insert_after(6, 3)
        1 -> 2 -> 3 -> 6 -> 4 -> 5 -> None
        >>> ll.insert_after(7, 5) # insert at tail
        1 -> 2 -> 3 -> 6 -> 4 -> 5 -> 7 -> None
        >>> ll.insert_after(8, 11) # insert at nonexistent
        Traceback (most recent call last):
        Exception: Target not in list
        """
        current_node = self.head
        while current_node and current_node.value != target:
            current_node = current_node.next
        if current_node:
            new_node = Node(value, current_node.next, current_node)
            current_node.next = new_node
            current_node.next.previous = new_node
            return self
        else:
            raise Exception("Target not in list")

    def insert_before(self, value, target):
        """
        Insert node just after first instance of target
        >>> ll = LinkedList([1,2,3,4])
        >>> ll.insert_before(6, 3)
        1 -> 2 -> 6 -> 3 -> 4 -> None
        >>> ll.insert_before(7, 1) # insert at head
        7 -> 1 -> 2 -> 6 -> 3 -> 4 -> None
        >>> ll.insert_before(8, 11) # insert at nonexistent
        Traceback (most recent call last):
        Exception: Target not in list
        """
        current_node = self.head
        if current_node.value == target:
            self.add_first(value)
            return self
        while current_node and current_node.value != target:
            current_node = current_node.next
        if current_node:
            new_node = Node(
                value, current_node, current_node.previous)
            current_node.previous.next = new_node
            current_node.previous = new_node
            return self
        else:
            raise Exception("Target not in list")

    def remove_first(self):
        """
        Remove node from head.
        >>> ll = LinkedList([1,2,3,4,5])
        >>> ll.remove_first()
        None -> 1 -> 2
        >>> print(ll)
        2 -> 3 -> 4 -> 5 -> None
        """
        removed_node = self.head
        self.head = removed_node.next
        self.head.previous = None
        return removed_node

    def remove_last(self):
        """
        Remove node from tail.
        >>> ll = LinkedList([1,2,3,4,5])
        >>> ll.remove_last()
        4 -> 5 -> None
        >>> print(ll)
        1 -> 2 -> 3 -> 4 -> None
        """
        removed_node = self.tail
        self.tail = removed_node.previous
        self.tail.next = None
        return removed_node

    def size(self):
        """
        Get size of linked list.
        >>> ll = LinkedList([1,2,3,4])
        >>> ll.size()
        4
        """
        return sum([1 for node in self])

    def search(self, value):
        """
        Search for value in list.
        >>> ll = LinkedList([1,2,3,4])
        >>> ll.search(3)
        2
        >>> ll.search(37)
        Traceback (most recent call last):
        Exception: Value not in list
        """
        for i, node in enumerate(self):
            if node.value == value:
                return i
        raise Exception("Value not in list")

    def reverse_iterative(self):
        """
        Reverse list.
        >>> ll = LinkedList([1,2,3,4])
        >>> ll.reverse_iterative()
        4 -> 3 -> 2 -> 1 -> None
        >>> print(ll.head)
        None -> 4 -> 3
        >>> print(ll.tail)
        2 -> 1 -> None
        """
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.previous, current_node.next = current_node.next, current_node.previous
            current_node = next_node
        self.head, self.tail = self.tail, self.head
        return self


if __name__ == "__main__":
    doctest.testmod()
