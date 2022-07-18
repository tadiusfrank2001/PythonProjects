"""

    Author: Tadius Frank

    The goal of this assignment is to implement an interactive
    game of Tic-tac-toe
    
"""
import random
import copy

computer = 'x'
human = 'o'


def init():
    """
    initialize the game board with 3*3 grid with `_` in each cell
    :return: (list) the game board
    """
    # Create 2D list
    return [['_' for i in range(3)] for j in range(3)]


def print_board(board):
    """
    Print the game board

    :param board: (list) the game board, which is a 2D list
    :return: None

    """
    print("Board:")
    print("="*6)

    # Print a 3 by 3 game board
    for row in board:
        for elem in row:
            print(elem + " ", end="")
        print()

    print("="*6)
    print()


def place(board, row, col, marker):
    """
    Place the player's marker (`x` or `o`) at cell (row, col)

    :param board: (list) the game board, which is a 2D list
    :param row: (int) the row index of the cell to place the marker
    :param col: (int) the col index of the cell to place the marker
    :param marker: (str) the player's game character
    :return: (list) the updated game board

    """
    # Find desired row with desired index in big list
    # then find to column with desired index in small list
    # Place marker at cell (row,col)
    board[row][col] = marker

    # Return the new board
    return board


def is_conflict(board, row, col):
    """
    Check if the demanded cell is already used

    :param board: (list) the game board, which is a 2D list
    :param row: (int) the row index of the requested cell
    :param col: (int) the col index of the requested cell
    :return: (bool) True if the cell is already used; otherwise, False

    """
    # if requested cell is occupied by a player return true
    if board[row][col] == "x" or board[row][col] == "o":
        return True
    # if requested cell is not occupied by a player return False
    elif board[row][col] == "_":
        return False


def validate_input(board, row, col):
    """
    Check if the human player input is valid based on the rules below:
        - row and col need to be single digit int number from 0, 1, 2
        - the requested cell at (row, col) is not used yet
    
    :param board: (list) the game board, which is a 2D list
    :param row: (str) the input row index
    :param col: (str) the input col index
    :return: (str) feedback to human player if input is
            invalid; "" (empty string) if input is valid

    """

    # Intialize list of valid index numbers
    valid_num = [0,1,2]
    # if string row or string col not digits return erroe message
    if not str(row).isdigit() or not str(col).isdigit():
        return("the index of BOTH row and col need to be SINGLE DIGITS from 0, 1, 2")
    # Change row and col to integers
    row = int(row)
    col = int(col)

    # if a row index and a col index can be found in the list it is valid
    if (row in valid_num) and (col in valid_num):
        #if the space is not occupied return an empty string
        if (is_conflict(board, row, col) == False):
            return ""
        elif (is_conflict(board, row, col) == True):
            return ("the selected cell ("+ str(row)+", "+ str(col)+ ") is not available")
    else:
        if not (row in valid_num) and not (col in valid_num):
            return ("BOTH row AND col indices have to be from 0, 1, or 2")
        # return error message when row index is not in the list
        if not (row in valid_num):
            return ("row index has to be from 0, 1, or 2 ")
        # return error message when col index is not in the list
        if not (col in valid_num):
            return ("col index has to be from 0, 1, or 2")


def row_win(board, player):
    """
    Check if the given player has a win in a row

    :param board: (list) the game board, which is a 2D list
    :param player: (str) the given player's marker `x` or `o`
    :return: (bool) True if there is a win in a row; otherwise False

    """
    # Check each row in board to if it is equal to the player's marker string
    # then assign a boolean value
    row_1= board[0][0] == board[0][1] == board[0][2] == player
    row_2 = board[1][0] == board[1][1] == board[1][2] == player
    row_3 = board[2][0] == board[2][1] == board[2][2] == player

    # any of the rows are True return true
    if row_1 or row_2 or row_3:
        return True
    # For other cases, return False 
    else:
        return False


def col_win(board, player):
    """
    Check if the given player has a win in a col

    :param board: (list) the game board, which is a 2D list
    :param player: (str) the given player's marker `x` or `o`
    :return: (bool) True if there is a win in a col; otherwise False

    """
    # Check each column in the board to see if it is equal to the player marker string
    # then assign a boolean value
    col_1 = board[0][0] == board[1][0] == board[2][0] == player
    col_2 = board[0][1] == board[1][1] == board[2][1] == player
    col_3 = board[0][2] == board[1][2] == board[2][2] == player
    
    # if any columns are True return True
    if col_1 or col_2 or col_3:
        return True
    # For other cases, return False
    else:
        return False 


def diag_win(board, player):
    """
    Check if the given player has a win in a diagonal direction

    :param board: (list) the game board, which is a 2D list
    :param player: (str) the given player's marker `x` or `o`
    :return: (bool) True if there is a win in a diagonal direction; otherwise False

    """

    # Check each diagonal in board to see if it equal to the player's marker string
    # then assign a boolean value to the diagonal
    diag_1 = board[0][0] == board[1][1] == board[2][2] == player
    diag_2 = board[2][0] == board[1][1] == board[0][2] == player

    # if the diagonals are True return True
    if diag_1 or diag_2:
        return True
    # For other cases return False
    else:
        return False

def is_win(board, player):
    """
    Check if the given player wins the game

    :param board: (list) the game board, which is a 2D list
    :param player: (str) the given player's marker `x` or `o`
    :return: (bool) True if the given player wins; otherwise False

    """
    # Call the functions for rows, columns, and diagonals
    # If any of there outputs is True then return true
    if row_win(board, player) or col_win(board, player) or diag_win(board, player):
        return True
    # For any other cases, return False
    else:
        return False 


def get_available_cells(board):
    """
    Obtain the row and col index of all the available cells

    :param board: (list) the game board, which is a 2D list
    :return: (list) a list of tuples in the form of (row, col)

    """
    # Initialize empty list
    space_list = []

    # Iterate through the indices of the 2D board list
    for row in range(len(board)):
        # Iterate through the indicies of each element in the row
        for element in range(len(board[row])):
            # if the list item is equal to an empty space (_) 
            # then append to space_list as tuples
            if board[row][element] == "_":
                space_list.append((row, element))
    # Return the new list of tuples
    return space_list


def computer_player(board):
    """
    Computer player randomly select an available cell and place the move

    :param board: (list) the game board, which is a 2D list
    :return: (list) the updated game board

    """  
    print("Computer placing...")

    # Utilize random.choice to select a random placement of the board from available space
    placement = random.choice(get_available_cells(board))

    # Assign index 0 to row index and index 1 to col index
    row = placement[0]
    col = placement[1]

    # Call place() to graph the coordinate on the board
    board = place(board, row, col, "x")

    # Print the board
    print_board(board)
    # Return the new board
    return board


def human_player(board):
    """
    Human player asks the user for valid input of row and col to place the move

    :param board: (list) the game board, which is a 2D list
    :return: (list) the updated board

    """
    # Ask user for input for rows and columns
    row = input("Please enter the row index: ")
    col = input("Please enter the col index: ")

    # while validate_input() function does not return an empty string
    while validate_input(board, row, col) != "":
        # Print Error for human
        print(validate_input(board, row, col))
        # Ask for new input until it is correct
        row = input("Please re-enter the row index: ")
        col = input("Please re-enter the col index: ")
    # Change rows and col to int
    row = int(row)
    col = int(col)
    
    # Graph the coordinates on the board
    board = place(board, row, col, "o")

    # Print board
    print_board(board)

    # Return board
    return board


def play_game(board, computer_first):
    """
    Play the game as specified below:
        - while game is not over, let the player continue the game
        - when game is over, print out the result (win/lost information)
    :param board: (list) the game board, which is a 2D list
    :param computer_first: (bool) True if computer player goes first; otherwise, False;
    :return: None

    """
    # while computer_first is the True boolean
    while computer_first == True:
        # Motion computer to play first
        board = computer_player(board)
        # if is_win() returns True for any player break the loop
        if (is_win(board, "x") == True) or (is_win(board, "o") == True):
            break
        # if get_available_cells() returns an empty list 
        # the board is full so break the loop
        elif get_available_cells(board) == []:
            break        
        # Motion human to play
        board = human_player(board)
        # Check if is_win is True for either players to break the loop
        if (is_win(board, "x") == True) or (is_win(board, "o") == True):
            break
        # if get_available_cells() returns an empty list 
        # the board is full so break the loop
        elif get_available_cells(board) == []:
            break

    # While computer_first is the False boolean
    while computer_first == False:
        # Motion human to play
        board = human_player(board)
        # if is_win() returns True for any player break the loop
        if (is_win(board, "x") == True) or (is_win(board, "o") == True):
            break
        # if get_available_cells() returns an empty list 
        # the board is full so break the loop
        elif get_available_cells(board) == []:
            break
        # Motion computer to play
        board = computer_player(board)
        # if is_win() returns True for any player break the loop
        if (is_win(board, "x") == True) or (is_win(board, "o") == True):
            break
        # if get_available_cells() returns an empty list 
        # the board is full so break the loop
        elif get_available_cells(board) == []:
            break

    # if is_win() is equal to true for the human player
    # human player won and computer lost 
    if is_win(board,"o") == True:
        name = "**** You Player (o) are the WINNER **** "
        loser = "*** Your Computer LOST :-[ ***"
    # if is_win() is equal to true for the computer player
    # computer player won and human lost 
    elif is_win(board, "x") == True:
        name = "**** Your Computer (x) is the WINNER!!! **** "
        loser = "*** You LOST :-[ ***"
    # For any other cases, the game is a draw
    else:
        name = "**** XO this is a TIED MATCH!! ***"
        loser = "*** NO one lost or won :-| ***"
    # Print results
    print(str(name)+"\n"+ str(loser))
    # Print final game board
    print_board(board)


def intelligent_computer_strategy(board):
    """
    an intelligent strategy for computer to select the row and col to place the move
    :param board: (list) the game board, which is a 2D list
    :return: (tuple) a tuple in the form of (row, col)
    """
    pass


def main():
    """
    welcome, ask the user to choose who goes first, then start the game
    """
    board = init()
    print("="*36)
    print("  Welcome to the Tic-Tac-Toe Game!")
    print("="*36)
    print()
    print_board(board)

    game_mode = input("Choose computer goes first or you go first?\n"
                      "1. Computer goes first.\n"
                      "2. I go first.\n"
                      "Please choose 1 or 2: ")

    print("\nGame start!")
    play_game(board, game_mode == '1')


if __name__ == "__main__":
    main()
