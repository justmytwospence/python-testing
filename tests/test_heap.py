import random

import pytest

from heap import BinaryHeap

class TestHeap:

    def verify_max_heap(self, heap):
        for node in range(0, len(heap)):
            node_value = heap.heap[node]

            left_node = heap.left(node)
            if heap.check_node_exists(left_node):
                left_value = heap.heap[left_node]
                assert node_value > left_value

            right_node = heap.right(node)
            if heap.check_node_exists(right_node):
                right_value = heap.heap[right_node]
                assert node_value > right_value

    @pytest.fixture
    def heap(self):
        return BinaryHeap(random.sample(range(100), 100))

    @pytest.fixture
    def empty_heap(self):
        return BinaryHeap([])

    @pytest.fixture
    def random_list(self):
        return random.sample(range(20), 20)

    def test_build_heap(self, heap):
        self.verify_max_heap(heap)

    def test_heappop(self, heap):
        popped = heap.heappop()
        assert popped == 99
        self.verify_max_heap(heap)
        popped = heap.heappop()
        assert popped == 98
        self.verify_max_heap(heap)

    def test_heappop_empty(self, empty_heap):
        assert empty_heap.heappop() is None

    def test_heapsort(self, random_list):
        sorted_list = BinaryHeap.heapsort(random_list)
        assert sorted_list
