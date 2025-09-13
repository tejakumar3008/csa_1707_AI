N = 8
def print_solution(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print()
def is_safe(board, row, col):
    for i in range(col):
        if board[row][i]:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j]:
            return False
    return True
def solve(board, col):
    if col >= N:
        print_solution(board)
        return True
    res = False
    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1
            res = solve(board, col + 1) or res
            board[i][col] = 0  # Backtrack
    return res
def solve_n_queens():
    board = [[0] * N for _ in range(N)]
    if not solve(board, 0):
        print("No solution exists")
solve_n_queens()
