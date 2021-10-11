class BinaryHeap:
    """Implementation of a maximum heap"""

    def __init__(self, values):
        self.heap = values
        self.build_max_heap()

    def __len__(self):
        return len(self.heap)

    def peek(self):
        return self.heap[0]

    def left(self, position):
        return int(position * 2 + 1)

    def right(self, position):
        return int(position * 2 + 2)

    def parent(self, position):
        if position == 0:
            return None
        else:
            return int((position - 1) // 2)

    def is_leaf(self, position):
        if position >= len(self) // 2:
            return True
        else:
            return False

    def check_node_exists(self, position):
        try:
            return self.heap[position] is not None
        except IndexError:
            return False

    def heapify(self, node):
        # bubble node down to correct position
        current_node = node
        while not self.is_leaf(current_node):

            # find node to swap with
            candidate_swap_nodes = [self.left(current_node),
                                    self.right(current_node)]
            candidate_swap_nodes = [node for node in candidate_swap_nodes
                                    if self.check_node_exists(node)]
            swap_node = max(candidate_swap_nodes, key=lambda i: self.heap[i])

            # swap node if current_node is larger
            current_node_value = self.heap[current_node]
            swap_node_value = self.heap[swap_node]
            if current_node_value < swap_node_value:
                self.heap[current_node], self.heap[swap_node] = self.heap[swap_node], self.heap[current_node]
            else:
                break
            current_node = swap_node

    def build_max_heap(self):
        for node in range(len(self) // 2, -1, -1):
            self.heapify(node)

    def heappush(self, value):
        # add item to end of heap
        self.heap.append(value)

        # restore heap invariant
        current_node = len(self) - 1
        while current_node:
            parent_node = self.parent(current_node)
            current_value = self.heap[current_node]
            parent_value = self.heap[parent_node]
            if current_value > parent_value:
                self.heap[current_node], self.heap[parent_node] = self.heap[parent_node], self.heap[current_node]
                current_node = parent_node
            else:
                break

    def heappop(self):
        if len(self) == 0:
            return None

        if len(self) == 1:
            return self.heap.pop()

        # move last node to root
        root_max = self.heap[0]
        new_root = self.heap.pop()

        # restore heap invariant
        self.heap[0] = new_root
        self.heapify(0)

        return root_max

    @staticmethod
    def heapsort(iterable):
        """O(n logn)"""
        heap = BinaryHeap(iterable)  # O(logn)
        sorted_list = []
        while heap.heap:  # O(n)
            sorted_list.insert(0, heap.heappop())
        return sorted_list
