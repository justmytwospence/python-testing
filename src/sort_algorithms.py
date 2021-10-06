import doctest
import random


def bubble_sort(items):
    """
    >>> bubble_sort([5,4,3,2,1])
    [1, 2, 3, 4, 5]
    >>> l = bubble_sort([random.randint(0,9) for _ in range(100)])
    >>> l == sorted(l)
    True
    """
    for i in range(len(items)):
        already_sorted = True
        for j in range(len(items) - 1 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                already_sorted = False
        if already_sorted:
            break
    return items


def insertion_sort(items, left=0, right=None):
    """
    >>> insertion_sort([5,4,3,2,1])
    [1, 2, 3, 4, 5]
    >>> l = insertion_sort([random.randint(0,9) for _ in range(100)])
    >>> l == sorted(l)
    True
    """
    if right is None:
        right = len(items)
    for i, current_item in enumerate(items[left:right]):
        j = i - 1
        while j >= left and current_item < items[j]:
            items[j + 1] = items[j]
            j -= 1
        items[j + 1] = current_item
    return items


def merge_sort(items):
    """
    >>> merge_sort([5,4,3,2,1])
    [1, 2, 3, 4, 5]
    >>> l = merge_sort([random.randint(0,9) for _ in range(100)])
    >>> l == sorted(l)
    True
    """
    if len(items) <= 1:
        return items
    midpoint = len(items) // 2
    left, right = items[:midpoint], items[midpoint:]
    return merge_sorted_lists(merge_sort(left), merge_sort(right))


def merge_sorted_lists(left, right):
    left_pointer, right_pointer = 0, 0
    return_list = []
    while len(return_list) < len(left) + len(right):
        left_item = left[left_pointer] if left_pointer < len(
            left) else float('inf')
        right_item = right[right_pointer] if right_pointer < len(
            right) else float('inf')
        if left_item < right_item:
            return_list.append(left_item)
            left_pointer += 1
        else:
            return_list.append(right_item)
            right_pointer += 1
    return return_list


def timsort(items):
    """
    >>> timsort([4,3,2,1])
    [1, 2, 3, 4]
    """
    # insertion sort chunks
    chunk_size = 32
    for chunk_start in range(0, len(items), chunk_size):
        chunk_end = min(chunk_start + chunk_size - 1, len(items))
        insertion_sort(items, chunk_start, chunk_end)
    size = chunk_size
    # merge sorted chunks
    while size < len(items):
        for start in range(0, len(items), size * 2):
            midpoint = start + size - 1
            end = min(start + size * 2 - 1, (len(items) - 1))
            merged_array = merge_sorted_lists(
                items[start:midpoint+1],
                items[midpoint + 1:end+1])
            items[start:start + len(merged_array)] = merged_array
        size *= 2
    return items

    # run insertion sort on each section


def quicksort(items, left=0, right=None):
    """
    >>> quicksort([5,4,3,2,1])
    [1, 2, 3, 4, 5]
    >>> l = quicksort([random.randint(0,9) for _ in range(100)])
    >>> l == sorted(l)
    True
    """
    if right is None:
        right = len(items) - 1
    if left < right:
        pivot = partition(items, left, right)
        quicksort(items, left, pivot - 1)
        quicksort(items, pivot + 1, right)
    return items


def partition(items, left, right):
    i = left
    j = right - 1
    p = random.randint(left, right)  # choose pivot
    items[p], items[right] = items[right], items[p]  # move it to the end
    pivot = items[right]
    while i < j:
        while i < right and items[i] < pivot:
            i += 1
        while j > left and items[j] >= pivot:
            j -= 1
        if i < j:
            items[i], items[j] = items[j], items[i]
    if items[i] > pivot:
        items[i], items[right] = items[right], items[i]
    return i


if __name__ == "__main__":
    doctest.testmod()
