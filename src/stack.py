class Stack:
    def __init__(self):
        self._storage = []

    def __len__(self):
        return len(self._storage)

    def push(self, item):
        self._storage.append(item)

    def pop(self):
        return self._storage.pop()
