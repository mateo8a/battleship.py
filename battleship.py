"""This program is a game that emulates the classic 'battleship' game. The board
is a square.
The ship takes up only one board space. The user specifies the amount of turns 
they want to play for, and also the size of the board."""

from random import randint #Import a function we'll need later.


def print_board(board):    #Prints the current status of the board
    for row in board:
        print " ".join(row)

#The position of the battleship is given by the following two functions
def random_row(board):
    return randint(0, len(board) - 1) 

def random_col(board):
    return randint(0, len(board) - 1)

#print ship_row
#print ship_col

if __name__=="__main__":

    board_size = int(raw_input("How big (N x N) do you want the board to be? Input N: "))

    board = [] #Set the board to an empty list.

    for x in range(board_size):
        board.append(["O"] * board_size) #We fill the board with "O"s to represent spaces that haven't been guessed yet.

    #Let's begin the game!
    print "Let's play Battleship!"
    print_board(board)

    ship_row = random_row(board)
    ship_col = random_col(board)

    turns = int(raw_input("For how many turns would you like to play? "))

    for turn in range(turns):
        print "Turn %d" %(turn + 1)
        guess_row = int(raw_input("Guess Row: "))
        guess_col = int(raw_input("Guess Col: "))
    
        if guess_row - 1 == ship_row and guess_col - 1 == ship_col:
            print "Congratulations! You sunk my battleship!"
            break
        else:
            if (guess_row  < 1 or guess_row > board_size) or (guess_col < 1 or guess_col > board_size):
                print "Oops, that's not even in the ocean."
            elif(board[guess_row - 1][guess_col - 1] == "X"):
                print "You guessed that one already."
            else:
                print "You missed my battleship!"
                board[guess_row - 1][guess_col - 1] = "X"

            print_board(board)
        if turn + 1 == turns:
            print "Game Over"