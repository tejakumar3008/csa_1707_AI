from heapq import heappop, heappush
class Graph:
    def __init__(self):
        self.edges = {}
        self.h = {}  
    def add_edge(self, u, v, cost):
        if u not in self.edges:
            self.edges[u] = []
        self.edges[u].append((v, cost))
    def set_heuristic(self, h):
        self.h = h
    def astar(self, start, goal):
        open_list = []
        heappush(open_list, (0 + self.h[start], 0, start, [start]))  # (f = g+h, g, node, path)
        closed_set = set()
        while open_list:
            f, g, node, path = heappop(open_list)
            if node == goal:
                return path, g 
            if node in closed_set:
                continue
            closed_set.add(node)
            for neighbor, cost in self.edges.get(node, []):
                if neighbor not in closed_set:
                    new_g = g + cost
                    new_f = new_g + self.h[neighbor]
                    heappush(open_list, (new_f, new_g, neighbor, path + [neighbor]))
        return None, float('inf')
graph = Graph()
graph.add_edge('A', 'B', 1)
graph.add_edge('A', 'C', 4)
graph.add_edge('B', 'D', 6)
graph.add_edge('B', 'E', 2)
graph.add_edge('C', 'F', 3)
graph.add_edge('E', 'F', 1)
graph.add_edge('D', 'G', 1)
graph.add_edge('F', 'G', 5)
graph.set_heuristic({
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 2,
    'E': 4,
    'F': 2,
    'G': 0
})
path, cost = graph.astar('A', 'G')
print("Best Path:", path)
print("Total Cost:", cost)
