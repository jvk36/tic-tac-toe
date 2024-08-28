# Initialize the board
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

# Function to display the board
def display_board():
    print("-------------")
    for row in board:
        print("|", row[0], "|", row[1], "|", row[2], "|")
        print("-------------")

# Function to check for a win
def check_win(player):
    # Check rows
    for row in board:
        if row.count(player) == 3:
            return True
    
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    
    return False

# Function to check if the board is full
def is_board_full():
    return all(cell != " " for row in board for cell in row)

# Function to get player input and update the board
def make_move(player):
    while True:
        try:
            row = int(input(f"Player {player}, enter row (0-2): "))
            col = int(input(f"Player {player}, enter column (0-2): "))
            
            if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == " ":
                board[row][col] = player
                return
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Please enter numbers between 0 and 2.")

if __name__ == "__main__":

    # Main game loop
    current_player = "X"
    while True:
        display_board()
        make_move(current_player)
        
        if check_win(current_player):
            display_board()
            print(f"Player {current_player} wins!")
            break
        
        if is_board_full():
            display_board()
            print("It's a draw!")
            break
        
        # Switch player
        current_player = "O" if current_player == "X" else "X"

    print("Game Over!")
