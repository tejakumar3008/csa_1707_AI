import heapq
def manhattan(state, goal):
    distance = 0
    for i in range(1, 9):
        x1, y1 = divmod(state.index(i), 3)
        x2, y2 = divmod(goal.index(i), 3)
        distance += abs(x1 - x2) + abs(y1 - y2)
    return distance
def get_neighbors(state):
    neighbors = []
    idx = state.index(0) 
    x, y = divmod(idx, 3)
    moves = [(-1,0),(1,0),(0,-1),(0,1)] 
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_idx = nx * 3 + ny
            new_state = list(state)
            new_state[idx], new_state[new_idx] = new_state[new_idx], new_state[idx]
            neighbors.append(tuple(new_state))
    return neighbors
def solve_puzzle(start, goal):
    frontier = []
    heapq.heappush(frontier, (0 + manhattan(start, goal), 0, start, []))
    visited = set()
    while frontier:
        est_total, cost, state, path = heapq.heappop(frontier)
        if state in visited:
            continue
        visited.add(state)
        if state == goal:
            return path + [state]
        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                heapq.heappush(frontier, (
                    cost + 1 + manhattan(neighbor, goal),
                    cost + 1,
                    neighbor,
                    path + [state]
                ))
    return None
start_state = (1, 2, 3,
               4, 0, 6,
               7, 5, 8)  
goal_state = (1, 2, 3,
              4, 5, 6,
              7, 8, 0)
solution = solve_puzzle(start_state, goal_state)
print("Steps to solve 8 Puzzle:")
for step in solution:
    for i in range(0, 9, 3):
        print(step[i:i+3])
    print()
