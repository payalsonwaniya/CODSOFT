# CodSoft AI Internship – Task 2
# Tic Tac Toe with AI (Random Moves)
# Created by Payal Sonwaniya

import random

def print_board(board):
    print()
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, columns, diagonals
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in zip(*board):
        if all(cell == player for cell in col):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def player_move(board):
    while True:
        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
            if board[row][col] == " ":
                return row, col
            else:
                print("⚠️ Cell already filled. Try again.")
        except:
            print("⚠️ Invalid input. Use numbers 0 to 2.")

def computer_move(board):
    return random.choice(get_empty_cells(board))

def play_game():
    board = [[" "]*3 for _ in range(3)]
    print("🎮 Welcome to My Tic Tac Toe – You (X) vs Computer (O)")

    for turn in range(9):
        print_board(board)
        if turn % 2 == 0:
            print("👉 Your Turn:")
            row, col = player_move(board)
            board[row][col] = "X"
        else:
            print("🤖 Computer's Turn:")
            row, col = computer_move(board)
            board[row][col] = "O"

        if check_winner(board, "X"):
            print_board(board)
            print("🎉 You Win!")
            return
        elif check_winner(board, "O"):
            print_board(board)
            print("💻 Computer Wins!")
            return

    print_board(board)
    print("😐 It's a Draw!")

play_game()
