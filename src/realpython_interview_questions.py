import doctest
from collections import Counter
from queue import PriorityQueue


def majority_element_indexes(lst):
    """
    >>> majority_element_indexes([1, 1, 2])
    [0, 1]
    >>> majority_element_indexes([1, 2])
    []
    >>> majority_element_indexes([])
    []
    """

    counter = Counter(lst)

    if len(counter) == 0:
        return []

    (majority_element, occasions_element) = counter.most_common(1)[0]
    if occasions_element > len(lst) // 2:
        return [i for i, x in enumerate(lst) if x == majority_element]
    else:
        return []


def keypad_string(keys):
    '''
    Given a string consisting of 0-9,
    find the string that is created using
    a standard phone keypad
    | 1        | 2 (abc) | 3 (def)  |
    | 4 (ghi)  | 5 (jkl) | 6 (mno)  |
    | 7 (pqrs) | 8 (tuv) | 9 (wxyz) |
    |     *    | 0 ( )   |     #    |
    You can ignore 1, and 0 corresponds to space
    >>> keypad_string("12345")
    'adgj'
    >>> keypad_string("4433555555666")
    'hello'
    >>> keypad_string("2022")
    'a b'
    >>> keypad_string("")
    ''
    >>> keypad_string("111")
    ''
    '''

    if len(keys) == 0:
        return ""

    keypad = {
        "1": [""],
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "y", "x", "z"],
        "0": [" "],
    }

    keys = list(keys)
    keys.append(None)
    output = []

    previous = keys[0]
    count = 0

    for current in keys[1:]:
        button = keypad[previous]
        if current == previous:
            count += 1
            if count == len(button):
                output.append(button[-1])
                count = 0
        else:
            output.append(button[count])
            count = 0
        previous = current
    return ''.join(output)


class Link:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val

    def __str__(self):
        if not self.next:
            return f"Link({self.val})"
        return f"Link({self.val}, {self.next})"


def merge_k_linked_lists(linked_lists):
    '''
    Merge k sorted linked lists into one
    sorted linked list.
    >>> print(merge_k_linked_lists([
    ...     Link(1, Link(2)),
    ...     Link(3, Link(4))
    ... ]))
    Link(1, Link(2, Link(3, Link(4))))
    >>> print(merge_k_linked_lists([
    ...     Link(1, Link(2)),
    ...     Link(2, Link(4)),
    ...     Link(3, Link(3)),
    ... ]))
    Link(1, Link(2, Link(2, Link(3, Link(3, Link(4))))))
    '''

    root = Link(None)
    current_node = root

    # construct priority queue
    pq = PriorityQueue()
    for node in linked_lists:
        pq.put(node)

    while not pq.empty():
        # pop off the next smallest node
        smallest = pq.get()  # O(1)
        # add it t1o the end of the output list
        current_node.next = smallest  # O(1)
        # advance pointer to the new tail of the output list
        current_node = smallest  # O(1)
        # add the next node that nodes list to candidates
        if smallest.next is not None:  # 0(1)
            pq.put(smallest.next)
    return root.next


if __name__ == "__main__":
    doctest.testmod()
