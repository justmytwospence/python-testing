class BSTNode:
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None

    def __repr__(self):
        left_value = self.left.value if self.left else None
        right_value = self.right.value if self.right else None
        return f'{self.value}, L={left_value}, R={right_value}'


class BinarySearchTree:

    def __init__(self, values):
        self.root = BSTNode(values.pop(0))
        [self.insert(node) for node in values]

    def find(self, value):
        """Find node with value"""
        current_node = self.root
        while current_node:
            if value < current_node.value:
                current_node = current_node.left
            elif value > current_node.value:
                current_node = current_node.right
            elif value == current_node.value:
                return current_node
        return None

    def insert(self, value):
        current_node = self.root

        # find the parent for the new node
        while current_node:
            parent_node = current_node
            if value > current_node.value:
                current_node = current_node.right
            elif value < current_node.value:
                current_node = current_node.left
            else:
                return self

        # create and insert new node
        new_node = BSTNode(value, parent=parent_node)
        if new_node.value < parent_node.value:
            parent_node.left = new_node
        if new_node.value > parent_node.value:
            parent_node.right = new_node

    def _find_successor(self, current_node):
        current_node = current_node.right
        while current_node.left:
            current_node = current_node.left
        return current_node

    def _find_predecessor(self, current_node):
        current_node = current_node.left
        while current_node.right:
            current_node = current_node.right
        return current_node

    def delete(self, value):
        node = self.find(value)
        children = (node.left, node.right)

        if all(children):  # 2 children

            # find successor node and pop it off
            successor_node = self._find_successor(node)
            if successor_node.parent.right == successor_node:
                successor_node.parent.right = None
            elif successor_node.parent.left == successor_node:
                successor_node.parent.left = None

            # splice successor into child nodes
            successor_node.right = node.right
            successor_node.left = node.left

            # splice successor into parent nodes
            if node.parent:
                if value > node.parent.value:
                    node.parent.right = successor_node
                elif value < node.parent.value:
                    node.parent.left = successor_node
            else:
                self.root = successor_node

        else:  # 0 or 1 child
            if value > node.parent.value:
                node.parent.right = node.right
            elif value < node.parent.value:
                node.parent.left = node.left

    def traverse_recursive(self, node=None, order='inorder'):
        if node is None:
            node = self.root
        left = self.traverse_recursive(node.left) if node.left else []  # list
        right = self.traverse_recursive(
            node.right) if node.right else []  # list
        if order == 'preorder':
            return [node.value] + left + right
        elif order == 'postorder':
            return left + right + [node.value]
        else:
            return left + [node.value] + right

    def traverse_iterative_inorder(self):
        visited_nodes = []
        node_stack = []
        current_node = self.root
        while current_node or node_stack:  # while there is a next node or nodes left in stack
            if current_node:  # get next left node
                node_stack.append(current_node)
                current_node = current_node.left
            else:  # hit leaf node, pop from stack and start again from it's right node
                current_node = node_stack.pop()
                visited_nodes.append(current_node.value)
                current_node = current_node.right
        return visited_nodes

    def traverse_iterative_preorder(self):
        visited_nodes = []
        node_stack = [self.root]
        while node_stack:
            current_node = node_stack.pop()
            visited_nodes.append(current_node.value)
            if current_node.right:
                node_stack.append(current_node.right)
            if current_node.left:
                node_stack.append(current_node.left)
        return visited_nodes

    def traverse_iterative_postorder(self):
        pass  # TODO
