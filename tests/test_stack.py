import sys

import pytest
from stack import Stack


class TestStack:

    @pytest.fixture
    def empty_stack(self):
        return Stack()

    @pytest.fixture
    def loaded_stack(self):
        stack = Stack()
        for item in range(10):
            stack.push(item)
        return stack

    def test_constructor(self, empty_stack):
        assert isinstance(empty_stack, Stack)
        assert len(empty_stack) == 0

    def test_push(self, empty_stack):
        empty_stack.push(37)
        assert empty_stack._storage[0] == 37
        assert len(empty_stack) == 1
        empty_stack.push(17)
        assert empty_stack._storage[1] == 17
        assert len(empty_stack) == 2

    def test_pop(self, loaded_stack):
        popped = loaded_stack.pop()
        assert popped == 9
        assert len(loaded_stack) == 9
        popped = loaded_stack.pop()
        assert popped == 8
        assert len(loaded_stack) == 8

    def test_pop_empty(self, empty_stack):
        with pytest.raises(IndexError):
            popped = empty_stack.pop()
