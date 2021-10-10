import pytest

from dijkstra import AdjacencyListGraph


class TestGraph:

    @pytest.fixture
    def graph(self):
        g = AdjacencyListGraph()
        g.add_node("A")
        g.add_node("B")
        g.add_node("C")
        g.add_node("D")
        g.add_node("E")
        g.add_node("F")
        g.add_node("G")
        g.add_node("Z")
        g.add_edge("A", "B", 2)
        g.add_edge("A", "C", 5)
        g.add_edge("B", "C", 6)
        g.add_edge("B", "E", 3)
        g.add_edge("C", "F", 8)
        g.add_edge("D", "E", 4)
        g.add_edge("E", "G", 9)
        g.add_edge("G", "F", 1)
        g.add_edge("G", "C", 2)
        g.add_edge("C", "A", 1)
        return g

    def test_constructor(self, graph):
        assert graph.nodes == set(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'Z'])
        assert graph.edges["A"]["C"] == 5
        assert graph.edges["A"]["B"] == 2
        assert "Z" not in graph.edges

    def get_shortest_path(self, graph):
        a_to_g = graph.get_shortest_path("A", "G")
        assert a_to_g == ["A", "B", "E", "G"]
        g_to_a = graph.get_shortest_path("G", "A")
        assert g_to_a == ["G", "C", "A"]
        g_to_b = graph.get_shortest_path("G", "B")
        assert g_to_b == ["G", "C", "A", "B"]
        # D is unreachable from any node
        with pytest.raises(Exception):
            graph.get_shortest_path("A", "D")
            graph.get_shortest_path("B", "D")
            graph.get_shortest_path("C", "D")
            graph.get_shortest_path("E", "D")
            graph.get_shortest_path("F", "D")
            graph.get_shortest_path("G", "D")

    def test_get_shortest_distance(self, graph):
        assert graph.get_shortest_distance("A", "B") == 2

    def test_caching(self, graph):
        assert len(graph.distances) == 0
        assert len(graph.paths) == 0
        graph.get_shortest_path("A", "B")
        assert len(graph.distances) == 1
        assert len(graph.paths) == 1
        graph.get_shortest_path("A", "C")
        assert len(graph.distances) == 1
        assert len(graph.paths) == 1
