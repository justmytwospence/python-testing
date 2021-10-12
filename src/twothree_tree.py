from bisect import bisect


class Node:
    def __init__(self, key, parent=None):
        self.keys = [key]
        self.parent = parent
        self.children = []

    def __repr__(self):
        return f"{self.parent} -> {self.keys} -> {self.children}"

    def __len__(self):
        return len(self.keys)

    def __lt__(self, other):
        return self.keys[0] < other.keys[0]

    def _is_leaf(self):
        return len(self.children) == 0

    def _add(self, new_node):
        # combine keys
        self.keys.extend(new_node.keys)
        self.keys.sort()

        # connect new_node's children to self
        for child in new_node.children:
            child.parent = self

        # connect self to new_nodes_children
        self.children.extend(new_node.children)
        self.children.sort()

        # start splitting if necessary
        if len(self) > 2:
            self._split()

    def _insert(self, new_node):
        if self._is_leaf():
            self._add(new_node)
        else:
            child_index = bisect(self.keys, new_node.keys[0])
            child = self.children[child_index]
            child._insert(new_node)

    def _split(self):
        # break apart new subtree
        left = Node(self.keys[0], parent=self)
        right = Node(self.keys[2], parent=self)
        self.keys = [self.keys[1]]

        if self.children:
            # connect old children new subtree
            self.children[0].parent = left
            self.children[1].parent = left
            self.children[2].parent = right
            self.children[3].parent = right

            # connect new subtree to old children
            left.children = [self.children[0], self.children[1]]
            right.children = [self.children[2], self.children[3]]

        # connect the subtree internally
        self.children = [left, right]

        # add new subtree's root to old parent
        if self.parent:
            self.parent.children.remove(self)
            self.parent._add(self)


class Tree:
    def __init__(self, root):
        self.root = Node(root)

    def _update_root(self):
        while self.root.parent:
            self.root = self.root.parent

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.root._insert(Node(value))
            self._update_root()
