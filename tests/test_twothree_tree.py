import pytest

from twothree_tree import Tree


class TestTree:

    @pytest.fixture
    def tree(self):
        t = Tree(10)
        return t

    def test_insert(self, tree):
        assert tree.root.keys == [10]
        tree.insert(9)
        assert tree.root.keys == [9, 10]

        tree.insert(11)  # root node should split
        assert tree.root.keys == [10]
        assert len(tree.root.children) == 2
        assert tree.root.children[0].keys == [9]
        assert tree.root.children[1].keys == [11]

        tree.insert(8)
        assert tree.root.keys == [10]
        assert len(tree.root.children) == 2
        assert tree.root.children[0].keys == [8, 9]
        assert tree.root.children[1].keys == [11]

        tree.insert(7)  # leaf node should split
        assert tree.root.keys == [8, 10]
        assert len(tree.root.children) == 3
        assert tree.root.children[0].keys == [7]
        assert tree.root.children[1].keys == [9]
        assert tree.root.children[2].keys == [11]

        tree.insert(12)
        tree.insert(13)  # leaf node and root should split
        assert tree.root.keys == [10]
        assert len(tree.root.children) == 2
        assert tree.root.children[0].keys == [8]
        assert tree.root.children[1].keys == [12]
        assert tree.root.children[0].children[0].keys == [7]
        assert tree.root.children[0].children[1].keys == [9]
        assert tree.root.children[1].children[0].keys == [11]
        assert tree.root.children[1].children[1].keys == [13]
