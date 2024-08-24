def print_board(board):
    print("\n".join(map(str, board)))

def check_winner(board):
    for i in range(3):
        if board[i][0]==board[i][1]==board[i][2] and board[i][0]!=' ': 
            return True
        if board[0][i]==board[1][i]==board[2][i] and board[0][i]!=' ': 
            return True
    if board[0][0]==board[1][1]==board[2][2] and board[0][0]!=' ': 
        return True
    if board[0][2]==board[1][1]==board[2][0] and board[0][2]!=' ': 
        return True
    return False

def make_move(board, letter, move):
    row = move // 3
    col = move % 3
    if board[row][col]!=' ':
        return False
    board[row][col] = letter
    return True

def tictactoe():
    board = [[' ']*3 for _ in range(3)]
    current_letter = 'X'
    moves_made = 0

    while not check_winner(board) and moves_made < 9:
        print_board(board)
        print("Current player:", current_letter)
        move = int(input("Enter your move (0-8): "))
        if make_move(board, current_letter, move):
            moves_made += 1
            if current_letter == 'X':
                current_letter = 'O'
            else:
                current_letter = 'X'
        else:
            print("Invalid move, try again")

    print_board(board)
    if check_winner(board):
        print("Player", current_letter, "wins!")
    else:
        print("It's a tie!")

tictactoe()