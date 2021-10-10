from collections import defaultdict


class AdjacencyListGraph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(dict)
        self.paths = {}
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].update({to_node: distance})

    def _compute_dijkstra(self, start_node):
        cost = {node: float('inf') for node in self.nodes}
        cost[start_node] = 0
        unvisited_nodes = set(self.nodes)
        parent = {}

        # update costs through the path of least resistance
        current_node = start_node
        while unvisited_nodes:

            # once a node is visited, don't return to it
            unvisited_nodes.remove(current_node)

            # for every neighbor
            neighbors = self.edges[current_node].items()
            for neighbor, edge_cost in neighbors:

                # update cost and parent if we've found a faster path to it
                potential_new_cost = cost[current_node] + edge_cost
                if potential_new_cost < cost[neighbor]:
                    cost[neighbor] = potential_new_cost
                    parent[neighbor] = current_node

            # proceed to cheapest unvisited node
            if unvisited_nodes:
                current_node = min(unvisited_nodes, key=cost.get)

        # cache paths and distances data
        self.paths[start_node] = parent
        self.distances[start_node] = cost

    def get_shortest_distance(self, start_node, target_node):
        # run dijkstra if it hasn't been run yet on start_node
        if self.distances.get(start_node) is None:
            self._compute_dijkstra(start_node)
        return self.distances[start_node][target_node]

    def get_shortest_path(self, start_node, target_node):

        # run dijkstra if it hasn't been run yet on start_node
        if self.paths.get(start_node) is None:
            self._compute_dijkstra(start_node)
        parent = self.paths[start_node]

        # work backwards to find the shortest path
        shortest_path = [target_node]
        current_node = target_node
        while current_node != start_node:
            try:
                current_node = parent[current_node]
            except KeyError:
                raise Exception(f'No path from {start_node} to {target_node}')
            shortest_path.insert(0, current_node)

        return shortest_path
