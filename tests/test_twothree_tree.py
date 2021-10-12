import pytest

from twothree_tree import Tree


class TestTree:

    @pytest.fixture
    def stump(self):
        t = Tree(10)
        return t

    @pytest.fixture
    def tree(self):
        t = Tree(10)
        t.insert(9)
        t.insert(11)
        t.insert(8)
        t.insert(7)
        t.insert(12)
        return t

    def test_insert(self, stump):
        assert stump.root.keys == [10]
        stump.insert(9)
        assert stump.root.keys == [9, 10]

        stump.insert(11)  # root node should split
        assert stump.root.keys == [10]
        assert len(stump.root.children) == 2
        assert stump.root.children[0].keys == [9]
        assert stump.root.children[1].keys == [11]

        stump.insert(8)
        assert stump.root.keys == [10]
        assert len(stump.root.children) == 2
        assert stump.root.children[0].keys == [8, 9]
        assert stump.root.children[1].keys == [11]

        stump.insert(7)  # leaf node should split
        assert stump.root.keys == [8, 10]
        assert len(stump.root.children) == 3
        assert stump.root.children[0].keys == [7]
        assert stump.root.children[1].keys == [9]
        assert stump.root.children[2].keys == [11]

        stump.insert(12)
        stump.insert(13)  # leaf node and root should split
        assert stump.root.keys == [10]
        assert len(stump.root.children) == 2
        assert stump.root.children[0].keys == [8]
        assert stump.root.children[1].keys == [12]
        assert stump.root.children[0].children[0].keys == [7]
        assert stump.root.children[0].children[1].keys == [9]
        assert stump.root.children[1].children[0].keys == [11]
        assert stump.root.children[1].children[1].keys == [13]

    def test_traverse(self, tree):
        # preorder
        nodes = tree.root.traverse_preorder()
        assert nodes == [[8, 10], [7], [9], [11, 12]]

        tree.insert(13)
        nodes = tree.root.traverse_preorder()
        assert nodes == [[10], [8], [7], [9], [12], [11], [13]]

        # inorder
        nodes = tree.root.traverse_inorder()
        assert nodes == [7, 8, 9, 10, 11, 12, 13]

    def test_find(self, tree):
        assert tree.find(10)
        assert tree.find(7)
        assert tree.find(11)
        assert not tree.find(37)
