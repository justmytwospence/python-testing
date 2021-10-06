import doctest
import functools

from sort_algorithms import merge_sorted_lists


def factorial_recursive(n):
    """
    >>> factorial_recursive(5)
    120
    """
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)


def deliver_presents_recursive(houses):
    """
    >>> deliver_presents_recursive(["Tim", "Bob", "Jon"])
    Delivered to Tim!
    Delivered to Bob!
    Delivered to Jon!
    """
    if len(houses) == 1:
        print(f"Delivered to {houses[0]}!")
    else:
        midpoint = len(houses) // 2
        deliver_presents_recursive(houses[:midpoint])
        deliver_presents_recursive(houses[midpoint:])


@functools.lru_cache
def fibonacci_recursive(position):
    """
    Return fibonacci sequence at position.
    >>> fibonacci_recursive(6)
    8
    """
    print(f"called with n={position}")
    if position == 0 or position == 1:
        return position
    return fibonacci_recursive(position - 2) + fibonacci_recursive(position - 1)


def merge_sort(items):
    """
    >>> merge_sort([5,4,3,2,1])
    [1, 2, 3, 4, 5]
    """
    if len(items) <= 1:
        return items
    else:
        midpoint = len(items) // 2
        sorted_left = merge_sort(items[:midpoint])
        sorted_right = merge_sort(items[midpoint:])
        return merge_sorted_lists(sorted_left, sorted_right)


if __name__ == "__main__":
    doctest.testmod()
