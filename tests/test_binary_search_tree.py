import pytest

from binary_search_tree import BSTNode, BinarySearchTree


class TestBSTNode:

    @pytest.fixture
    def node(self):
        return BSTNode(100)

    def test_constructor(self, node):
        assert isinstance(node, BSTNode)


class TestBinarySearchTree:

    @pytest.fixture
    def stump(self):
        return BinarySearchTree([100])

    @pytest.fixture
    def tree(self):
        return BinarySearchTree([100, 150, 50, 125, 75, 101, 200, 170])

    def test_constructor(self, stump):
        assert isinstance(stump, BinarySearchTree)

    def test_insert(self, stump):
        stump.insert(50)
        stump.insert(150)
        assert stump.root.value == 100
        assert stump.root.left.value == 50
        assert stump.root.right.value == 150

    def test_find(self, tree):
        assert isinstance(tree.find(50), BSTNode)
        assert not tree.find(37)

    def test_find_successor(self, tree):
        successor = tree._find_successor(tree.root)
        assert successor.value == 101
        successor = tree._find_successor(tree.root.right)
        assert successor.value == 170
        assert isinstance(successor.parent, BSTNode)

    def test_find_predecessor(self, tree):
        predecessor = tree._find_predecessor(tree.root)
        assert predecessor.value == 75
        predecessor = tree._find_predecessor(tree.root.right)
        assert predecessor.value == 125

    def test_delete_root(self, tree):
        assert tree.root.value == 100
        tree.delete(100)
        assert tree.root.value == 101

    def test_delete(self, tree):
        assert tree.root.right.value == 150
        tree.delete(150)
        assert tree.root.right.value == 170

    def test_traverse_recursive_inorder(self, tree):
        nodes = tree.traverse_recursive(order='inorder')
        assert len(nodes) == 8

    def test_traverse_iterative_inorder(self, tree):
        nodes = tree.traverse_iterative_inorder()
        assert nodes == [50, 75, 100, 101, 125, 150, 170, 200]

    def test_traverse_iterative_preorder(self, tree):
        nodes = tree.traverse_iterative_preorder()
        assert nodes == [100, 50, 75, 150, 125, 101, 200, 170]

    @pytest.mark.xfail
    def test_traverse_iterative_postorder(self, tree):
        nodes = tree.traverse_iterative_postorder()
        assert nodes == [100, 50, 75, 150, 125, 101, 200, 170]
