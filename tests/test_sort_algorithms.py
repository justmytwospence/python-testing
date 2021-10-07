import random

import pytest
from sort_algorithms import bubble_sort



class TestBubbleSort():
    def test_random_bubble_sort(self):
        input = [random.randint(0, 10) for _ in range(100)]
        expected = sorted(input)
        actual = bubble_sort(input)
        assert actual == expected

    def test_sorted_bubble_sort(self):
        input = [x for x in range(100)]
        expected = input
        actual = bubble_sort(input)
        assert actual == expected

    def test_empty_bubble_sort(self):
        input = []
        expected = []
        actual = bubble_sort(input)
        assert actual == expected

    def test_integer_bubble_sort(self):
        input = 3
        with pytest.raises(TypeError) as e:
            bubble_sort(input)
