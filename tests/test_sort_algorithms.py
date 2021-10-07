import random

import pytest
from sort_algorithms import bubble_sort, insertion_sort, merge_sort, quicksort

algorithms = [
    bubble_sort,
    insertion_sort,
    merge_sort,
    quicksort
]


class TestSort:

    @pytest.fixture
    def random_list(self):
        return [random.randint(0, 10) for _ in range(100)]

    @pytest.fixture
    def sorted_list(self):
        return [x for x in range(100)]

    @pytest.fixture
    def empty_list(self):
        return []

    @pytest.mark.parametrize("algorithm", algorithms)
    def test_random(self, algorithm, random_list):
        expected = sorted(random_list)
        actual = algorithm(random_list)
        assert actual == expected

    @pytest.mark.parametrize("algorithm", algorithms)
    def test_sorted(self, algorithm, sorted_list):
        expected = sorted_list
        actual = algorithm(sorted_list)
        assert actual == expected

    @pytest.mark.parametrize("algorithm", algorithms)
    def test_empty(self, algorithm, empty_list):
        actual = algorithm(empty_list)
        assert actual == empty_list

    @pytest.mark.parametrize("algorithm", algorithms)
    def test_integer(self, algorithm):
        input = 3
        with pytest.raises(TypeError) as e:
            algorithm(input)
