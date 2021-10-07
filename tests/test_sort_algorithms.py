import random

import pytest
from sort_algorithms import bubble_sort, insertion_sort


@pytest.fixture
def random_list():
    return [random.randint(0, 10) for _ in range(100)]


@pytest.fixture
def sorted_list():
    return [x for x in range(100)]


@pytest.fixture
def empty_list():
    return []


class TestBubbleSort:

    def test_random_bubble_sort(self, random_list):
        expected = sorted(random_list)
        actual = bubble_sort(random_list)
        assert actual == expected

    def test_sorted_bubble_sort(self, sorted_list):
        expected = sorted_list
        actual = bubble_sort(sorted_list)
        assert actual == expected

    def test_empty_bubble_sort(self, empty_list):
        actual = bubble_sort(empty_list)
        assert actual == empty_list

    def test_integer_bubble_sort(self):
        input = 3
        with pytest.raises(TypeError) as e:
            bubble_sort(input)


class TestInsertionSort:

    def test_random_insertion_sort(self, random_list):
        expected = sorted(random_list)
        actual = insertion_sort(random_list)
        assert actual == expected

    def test_sorted_insertion_sort(self, sorted_list):
        expected = sorted_list
        actual = insertion_sort(sorted_list)
        assert actual == expected

    def test_empty_insertion_sort(self, empty_list):
        actual = insertion_sort(empty_list)
        assert actual == empty_list
