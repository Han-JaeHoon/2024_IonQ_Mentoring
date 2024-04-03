import time
import psutil
import os

def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_n_queens_util(board, col, n):
    if col >= n:  # If all queens are placed successfully
        return True
    
    for i in range(n):
        if board[i][col] == 1:  # Skip the column if a queen is pre-placed
            if solve_n_queens_util(board, col + 1, n):
                return True
        elif is_safe(board, i, col, n):
            board[i][col] = 1
            if solve_n_queens_util(board, col + 1, n):
                return True
            board[i][col] = 0  # Backtrack if not solution
    return False

def pre_place_queens(board, n):
    for placed in range(2):
        user_input = input(f"Do you want to place queen {placed+1}? (y/n): ").strip().lower()
        if user_input == 'n':
            break  # Skip placing more queens
        
        print(f"Place queen {placed+1}:")
        row = int(input("Enter row (0-indexed): "))
        col = int(input("Enter column (0-indexed): "))
        if row >= n or col >= n or board[row][col] == 1 or not is_safe(board, row, col, n):
            print("Invalid or unsafe position. Skipping this queen.")
            continue
        board[row][col] = 1

def solve_n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    pre_place_queens(board, n)
    if not solve_n_queens_util(board, 0, n):
        return "Solution does not exist"
    return board

if __name__ == "__main__":
    n = int(input("Enter the number of queens (N): "))
    start_time = time.time()
    process = psutil.Process(os.getpid())
    start_memory = process.memory_info().rss / 1024
    solution = solve_n_queens(n)
    end_memory = process.memory_info().rss / 1024
    end_time = time.time()

    print("Solution:")
    if isinstance(solution, str):
        print(solution)
    else:
        for row in solution:
            print(' '.join(['Q' if cell == 1 else '.' for cell in row]))
    
    print(f"CPU Time: {end_time - start_time} seconds")
    print(f"Memory Usage: {end_memory - start_memory} KB")
