from itertools import permutations
def travelling_salesman(graph, start):
    vertices = list(range(len(graph)))
    vertices.remove(start)
    min_path = float('inf')
    best_path = []
    for perm in permutations(vertices):
        current_cost = 0
        k = start
        for j in perm:
            current_cost += graph[k][j]
            k = j
        current_cost += graph[k][start] 
        if current_cost < min_path:
            min_path = current_cost
            best_path = [start] + list(perm) + [start]
    return min_path, best_path
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
min_cost, best_path = travelling_salesman(graph, 0)
print("Minimum Cost:", min_cost)
print("Best Path:", best_path)
