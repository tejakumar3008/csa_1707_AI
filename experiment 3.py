from collections import deque
def water_jug_solver(jug1, jug2, target):
    visited = set()
    q = deque()
    q.append((0, 0))
    visited.add((0, 0))
    while q:
        a, b = q.popleft()
        print(f"({a}, {b})")
        if a == target or b == target:
            print("\n✅ Target achieved!")
            return True
        next_states = [
            (jug1, b),  
            (a, jug2),  
            (0, b),    
            (a, 0),    
            (a - min(a, jug2 - b), b + min(a, jug2 - b)),
            (a + min(b, jug1 - a), b - min(b, jug1 - a))
        ]
        for state in next_states:
            if state not in visited:
                visited.add(state)
                q.append(state)
    print("❌ No solution possible")
    return False
water_jug_solver(4, 3, 2)
