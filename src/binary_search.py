import doctest


def binary_iterative(elements, search_item):
    """
    Binary search
    >>> binary_iterative([1,2,3,4], 3)
    
    """
    left, right = 0, len(elements) - 1
    while left <= right:
        midpoint = (left + right) // 2
        if elements[midpoint] == search_item:
            return midpoint
        elif elements[midpoint] < search_item:
            left = midpoint + 1
        elif elements[midpoint] > search_item:
            right = midpoint - 1
    return None


def binary_leftmost(elements, search_item):
    tentative = binary_iterative(elements, search_item)
    if tentative is None:
        return None
    while elements[tentative] == search_item and tentative >= 0:
        tentative -= 1
    return tentative + 1


def binary_recursive(elements, search_item, dex_mod=0):
    """
    :elements: list
    :search_item: int
    :dex_mod: int

    >>> binary_recursive([1,2,3,4,5], 4)
    3
    """

    if len(elements) > 0:
        midpoint = len(elements) // 2
        if elements[midpoint] == search_item:
            return midpoint + dex_mod
        elif elements[midpoint] > search_item:
            return binary_recursive(elements[:midpoint], search_item, dex_mod)
        elif elements[midpoint] < search_item:
            dex_mod += midpoint
            return binary_recursive(elements[midpoint+1:], search_item, dex_mod + 1)


if __name__ == "__main__":
    doctest.testmod()
