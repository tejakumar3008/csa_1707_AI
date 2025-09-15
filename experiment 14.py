import math
def alphabeta(depth, node_index, is_max, scores, alpha, beta, height):
    if depth == height:
        return scores[node_index]
    if is_max: 
        best = -math.inf
        for i in range(2):  # two children for each node
            val = alphabeta(depth + 1, node_index * 2 + i, False, scores, alpha, beta, height)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:  
        best = math.inf
        for i in range(2):  
            val = alphabeta(depth + 1, node_index * 2 + i, True, scores, alpha, beta, height)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best
scores = [3, 5, 6, 9, 1, 2, 0, -1]
height = int(math.log2(len(scores)))
print("Leaf Nodes:", scores)
print("Optimal Value (using Alpha-Beta Pruning):",
      alphabeta(0, 0, True, scores, -math.inf, math.inf, height))
