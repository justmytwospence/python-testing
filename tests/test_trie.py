import pytest
from trie import Trie


class TestTrie:

    @pytest.fixture
    def trie(self):
        t = Trie()
        t.add("foo")
        t.add("bar")
        t.add("foobar")
        t.add("foobaz")
        return t

    def test_constructor(self, trie):
        isinstance(trie, Trie)

    def test_contains(self, trie):
        assert trie.contains("foo")
        assert trie.contains("bar")
        assert trie.contains("foobar")
        assert trie.contains("foobaz")
        assert not trie.contains("foobat")

    def test_traverse(self, trie):
        expected_value = [None, 'f', 'o', 'o',
                          'b', 'a', 'r', 'z', 'b', 'a', 'r']
        actual_value = [n.char for n in trie.root.traverse_preorder()]
        assert actual_value == expected_value

    def test_remove_no_prefix(self, trie):
        trie.remove("bar")
        assert trie.contains("foo")
        assert not trie.contains("bar")
        assert trie.contains("foobar")
        assert trie.contains("foobaz")

    def test_remove_is_prefix(self, trie):
        trie.remove("foo")
        assert not trie.contains("foo")
        assert trie.contains("bar")
        assert trie.contains("foobar")
        assert trie.contains("foobaz")

    def test_remove_has_prefix(self, trie):
        trie.remove("foobaz")
        assert trie.contains("foo")
        assert trie.contains("bar")
        assert trie.contains("foobar")
        assert not trie.contains("foobaz")
