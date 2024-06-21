def solve_n_queens(n):
    def print_board(board):
        for row in board:
            print(" ".join(row))
        print("\n")

    def is_safe(board, row, col):
        # Check this row on left side

        for i in range(col):
            if board[row][i] == 'Q':
                return False

        # Check upper diagonal on left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False

        # Check lower diagonal on left side
        for i, j in zip(range(row, n, 1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False

        return True

    def solve(board, col):
        if col >= n:
            solutions.append([row[:] for row in board])
            return True

        res = False
        for i in range(n):
            if is_safe(board, i, col):
                board[i][col] = 'Q'
                res = solve(board, col + 1) or res
                board[i][col] = '.'

        return res

    solutions = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    solve(board, 0)
    return solutions

# Example usage
n = 4
solutions = solve_n_queens(n)
for solution in solutions:
    for row in solution:
        print(" ".join(row))
    print("\n")
