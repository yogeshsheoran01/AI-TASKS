import math

# Global game state variables
board = [" " for _ in range(9)]  # Represents the 3x3 tic-tac-toe board
player_symbol = "X"              # Player's symbol ("X" or "O")
ai_symbol = "O"                  # AI's symbol ("X" or "O")
player_wins = 0                  # Number of games player has won
ai_wins = 0                      # Number of games AI has won
draws = 0                        # Number of draws
move_history = []                # List to keep track of moves made

# Print the current game board
def print_board():
    print("\nCurrent Board:")
    for i in range(3):
        row = board[i*3:(i+1)*3]
        print(" | ".join(row))
        if i < 2:
            print("-" * 9)
    print()

# Print a guide showing board positions (1-9)
def print_position_guide():
    print("Position Guide:")
    guide = [str(i+1) for i in range(9)]
    for i in range(3):
        print(" | ".join(guide[i*3:(i+1)*3]))
        if i < 2:
            print("-" * 9)
    print()

# Check if the given player has won on board b
def is_winner(b, player):
    # All possible win combinations (rows, columns, diagonals)
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    # Check if any win combination is satisfied
    return any(all(b[i] == player for i in combo) for combo in win_combinations)

# Check if the board is full (draw)
def is_draw(b):
    return " " not in b

# Get list of available (empty) positions on board b
def get_available_moves(b):
    return [i for i, val in enumerate(b) if val == " "]

# Minimax algorithm for AI decision making
def minimax(b, depth, is_maximizing):
    # Base cases: check for terminal states
    if is_winner(b, ai_symbol):
        return 1
    if is_winner(b, player_symbol):
        return -1
    if is_draw(b):
        return 0

    # Maximizing for AI
    if is_maximizing:
        best_score = -math.inf
        for move in get_available_moves(b):
            b[move] = ai_symbol
            score = minimax(b, depth + 1, False)
            b[move] = " "
            best_score = max(score, best_score)
        return best_score
    # Minimizing for player
    else:
        best_score = math.inf
        for move in get_available_moves(b):
            b[move] = player_symbol
            score = minimax(b, depth + 1, True)
            b[move] = " "
            best_score = min(score, best_score)
        return best_score

# AI makes its move using minimax
def ai_move():
    best_score = -math.inf
    best_move = None
    # Evaluate all possible moves
    for move in get_available_moves(board):
        board[move] = ai_symbol
        score = minimax(board, 0, False)
        board[move] = " "
        if score > best_score:
            best_score = score
            best_move = move
    # Make the best move
    board[best_move] = ai_symbol
    move_history.append((ai_symbol, best_move + 1))

# Player makes their move by input
def player_move():
    while True:
        try:
            move = int(input(f"Your turn ({player_symbol}). Choose (1-9): ")) - 1
            # Check if move is valid
            if 0 <= move < 9 and board[move] == " ":
                board[move] = player_symbol
                move_history.append((player_symbol, move + 1))
                break
            else:
                print("❌ Invalid move. Try again.")
        except ValueError:
            print("❌ Please enter a number between 1 and 9.")

# Choose player symbol
def choose_symbol():
    global player_symbol, ai_symbol
    while True:
        choice = input("Do you want to be X or O? (X goes first): ").upper()
        if choice in ["X", "O"]:
            player_symbol = choice
            ai_symbol = "O" if choice == "X" else "X"
            break
        else:
            print("Please choose either 'X' or 'O'.")

# Reset the game state
def reset_game():
    global board, move_history
    board = [" " for _ in range(9)]
    move_history = []

# Show move history
def show_history():
    print("\n📜 Move History:")
    for symbol, pos in move_history:
        print(f"{symbol} ➜ {pos}")
    print()

# Show game statistics
def show_stats():
    print("\n📊 Game Statistics:")
    print(f"You Wins: {player_wins}")
    print(f"AI Wins: {ai_wins}")
    print(f"Draws: {draws}")
    print()

# Play one full game
def play_game():
    global player_wins, ai_wins, draws

    reset_game()         # Reset board and history
    choose_symbol()      # Player chooses symbol
    print_position_guide()  # Show position guide
    print_board()        # Show empty board

    turn = "X"           # X always goes first
    while True:
        if turn == player_symbol:
            player_move()    # Player's turn
        else:
            print("🤖 AI is making a move...")
            ai_move()        # AI's turn

        print_board()        # Show board after move

        # Check for win/draw conditions
        if is_winner(board, player_symbol):
            print("🎉 Congratulations! You win!")
            player_wins += 1
            break
        elif is_winner(board, ai_symbol):
            print("😢 You lost! AI wins.")
            ai_wins += 1
            break
        elif is_draw(board):
            print("🤝 It's a draw!")
            draws += 1
            break

        # Switch turn
        turn = ai_symbol if turn == player_symbol else player_symbol

    show_history()   # Show moves made
    show_stats()     # Show stats

# Game loop
def main():
    print("🧠 Welcome to Unbeatable Tic-Tac-Toe AI!")
    while True:
        play_game()
        again = input("Do you want to play again? (yes/no): ").lower()
        if again not in ["yes", "y"]:
            print("👋 Goodbye! Thanks for playing.")
            break

if __name__ == "__main__":
    main()
