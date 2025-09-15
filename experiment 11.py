def is_safe(node, color, assignment, graph):
    for neighbor in graph[node]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True
def backtrack(graph, colors, assignment, nodes, index=0):
    if index == len(nodes):
        return assignment
    node = nodes[index]
    for color in colors:
        if is_safe(node, color, assignment, graph):
            assignment[node] = color
            result = backtrack(graph, colors, assignment, nodes, index + 1)
            if result:
                return result
            assignment.pop(node)
    return None
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'C', 'E'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['A', 'C', 'E'],
    'E': ['B', 'C', 'D']
}
colors = ['Red', 'Green', 'Blue']
solution = backtrack(graph, colors, {}, list(graph.keys()))
print("Map Coloring Solution:")
if solution:
    for region, color in solution.items():
        print(f"{region} -> {color}")
else:
    print("No solution found")
