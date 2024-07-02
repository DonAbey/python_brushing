import os
import random

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    

def display_board(board):
    clear()
    for i in range(0, len(board), 3):
        print(" | ".join(board[i:i+3]))


def player_input():
    '''
    OUTPUT = (Player1 marker, Player2 marker)
    '''
    while True:
        player1 = input("Player 1: Pick a marker 'X' or 'O': ").upper()
        if player1 not in ['X', 'O']:
            print("Please enter a valid input!")
        else:
            player2 = 'O' if player1 == 'X' else 'X'
            return (player1, player2)


def place_marker(board, marker, position):
    board[position - 1] = marker
    display_board(board)
    
def win_check(board, marker):
    # Checking all rows, columns, and diagonals
    return ((board[0] == board[1] == board[2] == marker) or
            (board[3] == board[4] == board[5] == marker) or
            (board[6] == board[7] == board[8] == marker) or
            (board[0] == board[3] == board[6] == marker) or
            (board[1] == board[4] == board[7] == marker) or
            (board[2] == board[5] == board[8] == marker) or
            (board[0] == board[4] == board[8] == marker) or
            (board[2] == board[4] == board[6] == marker))
    

def choose_first():
    return 'Player 1' if random.randint(0, 1) == 0 else 'Player 2'
    
def space_check(board, position):
    return board[position - 1] == ' '

def full_board_check(board):
    return all(space != ' ' for space in board)

def player_choice(board):
    while True:
        position = input('Pick an index position (1-9): ')
        if position.isdigit():
            position = int(position)
            if position in range(1, 10) and space_check(board, position):
                return position
            else:
                print('Please enter an input within the range and select an empty position.')
        else:
            print('Sorry, invalid input')
    
def replay():
    choice = input("Play again [Y/N]: ").upper()
    return choice == 'Y'


# While loop to keep running the game
print("Welcome to Tic Tac Toe game!")
while True:
    # Setting board
    board = [' '] * 9
    display_board(board)
    # Setting markers for players
    player1_marker, player2_marker = player_input()
    # Selecting player
    turn = choose_first()
    print(turn + " will go first")
    # Verifying to play the game
    play_game = input("Ready to play? [Y/N]: ").upper()
    game_on = play_game == 'Y'
        
    while game_on:
        if turn == 'Player 1':
            # Choosing position
            position = player_choice(board)
            # Placing marker
            place_marker(board, player1_marker, position)            
            # Checking if won
            if win_check(board, player1_marker):
                display_board(board)
                print("Player 1 has won the game!")
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("Game is a tie!")
                    game_on = False
                else:
                    turn = "Player 2"
        else:
            # Choosing position
            position = player_choice(board)
            # Placing marker
            place_marker(board, player2_marker, position)            
            # Checking if won
            if win_check(board, player2_marker):
                display_board(board)
                print("Player 2 has won the game!")
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("Game is a tie!")
                    game_on = False
                else:
                    turn = "Player 1"
    
    if not replay():
        break
