def print_solution(board):
    for row in board:
        print(" ".join("Q" if cell == 1 else "." for cell in row))

def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
    return True

def solve_n_queens_util(board, col):
    if col >= len(board):
        return True
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            if solve_n_queens_util(board, col + 1):
                return True
            board[i][col] = 0
    return False

def solve_n_queens():
    n = 8
    board = [[0] * n for _ in range(n)]
    if not solve_n_queens_util(board, 0):
        print("Solution does not exist")
        return False
    print_solution(board)
    return True

if __name__ == '__main__':
    solve_n_queens()
