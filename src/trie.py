class Node:
    def __init__(self, char, parent=None):
        self.char = char
        self.parent = parent
        self.children = {}
        self.end_of_string = False

    def traverse_preorder(self):
        if not self.children:
            yield self
        else:
            yield self
            for child in self.children.values():
                yield from child.traverse_preorder()


class Trie:
    def __init__(self):
        self.root = Node(None, parent=None)

    def add(self, string):
        string = list(string)
        current_node = self.root
        for char in string:
            if not current_node.children.get(char):
                current_node.children[char] = Node(char, parent=current_node)
            current_node = current_node.children[char]
        current_node.end_of_string = True

    def find(self, string):
        string = list(string)
        current_node = self.root
        for char in string:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return None
        if current_node.end_of_string:
            return current_node

    def contains(self, string):
        if self.find(string):
            return True
        else:
            return False

    def remove(self, string):
        to_remove = self.find(string)  # find the node

        # if it is a prefix, just remove the end_of_string marker
        potential_termina = [node.end_of_string
                             for node in to_remove.traverse_preorder()]
        if any(potential_termina):
            to_remove.end_of_string = False

        # otherwise, sever just below the next highest terminus
        else:
            while not to_remove.parent.end_of_string:
                to_remove = to_remove.parent
            to_remove.parent.children[to_remove.char] = None
