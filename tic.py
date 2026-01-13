#!/usr/bin/python3

def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("-" * 9)

def check_winner(board):
    # Rows
    for row in board:
        if row[0] != " " and row[0] == row[1] == row[2]:
            return row[0]

    # Columns
    for col in range(3):
        if board[0][col] != " " and board[0][col] == board[1][col] == board[2][col]:
            return board[0][col]

    # Diagonals
    if board[0][0] != " " and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] != " " and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]

    return None

def board_full(board):
    return all(cell != " " for row in board for cell in row)

def read_int(prompt):
    while True:
        s = input(prompt).strip()
        try:
            v = int(s)
        except ValueError:
            print("Invalid input. Please enter a number (0, 1, or 2).")
            continue
        if v not in (0, 1, 2):
            print("Out of range. Please enter 0, 1, or 2.")
            continue
        return v

def tic_tac_toe():
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        winner = check_winner(board)
        if winner is not None:
            print("Player " + winner + " wins!")
            break

        if board_full(board):
            print("It's a draw!")
            break

        row = read_int("Enter row (0, 1, or 2) for player " + player + ": ")
        col = read_int("Enter column (0, 1, or 2) for player " + player + ": ")

        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        board[row][col] = player
        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()