def inputPosition(): # position on board 
    pos = int(input("Insert index of board position : ")) # users input for placement of letter on the board
    return pos

def checkMove(pos): 
    """
    Checks if move being played is a valid move or not
    return boolean True for valid move and False for invalid moves
    """
    valid_moves = list(range(1,10))
    if pos not in valid_moves:
       print("Invalid move!")
       return False
    else:
        return True 

def printBoard(curBoard):
    """ Displays the current state of the board to screen
    """
    from IPython.display import clear_output # Only works in a jupyter notebook
    clear_output() 
    print("\n\t {}\t | \t {} \t | \t {}".format(curBoard[0][0],curBoard[0][1],curBoard[0][2]))
    print("--------------------------------------------------")
    print("\n\t {}\t | \t {} \t | \t {}".format(curBoard[1][0],curBoard[1][1],curBoard[1][2]))
    print("--------------------------------------------------")
    print("\n\t {}\t | \t {} \t | \t {}".format(curBoard[2][0],curBoard[2][1],curBoard[2][2]))
    print("\n\n")

def boardFunc(board,position,letter): 
    """
    takes in the three args, the board, position of x or piece to be placed on board, and currenponding letter( x or o)
    function updates the board location and returns True if update was made and False for updates not made
    """
    updateStatus = False
    if position == board[0][0]:
        board[0][0] = letter
        updateStatus = True
    elif position == board[0][1]:
        board[0][1] = letter
        updateStatus = True
    elif position == board[0][2]:
        board[0][2] = letter
        updateStatus = True

    elif position == board[1][0]:
        board[1][0] = letter
        updateStatus = True
    elif position == board[1][1]:
        board[1][1] = letter
        updateStatus = True
    elif position == board[1][2]:
        board[1][2] = letter
        updateStatus = True

    elif position == board[2][0]:
        board[2][0] = letter
        updateStatus = True
    elif position == board[2][1]:
        board[2][1] = letter
        updateStatus = True
    elif position == board[2][2]:
        board[2][2] = letter
        updateStatus = True

    return board, updateStatus 

def winCheck(board): 
    """takes in a boards current state of play and analyses it for a win. If it returns True a player has won, if it returns False 
    the game has ended in a draw   
    """                   
    winStatus = False 

    # Checking horizontal moves
    if(board[0][0] == board[0][1] == board[0][2]):
        winStatus = True
    elif (board[1][0] == board[1][1] == board[1][2]):
        winStatus = True
    elif (board[2][0] == board[2][1] == board[2][2]):
        winStatus = True

    # Checking vertical moves
    elif (board[0][0] == board[1][0] == board[2][0]):
        winStatus = True
    elif (board[0][1] == board[1][1] == board[2][1]):
        winStatus = True
    elif (board[0][2] == board[1][2] == board[2][2]):
        winStatus = True

    # Checking diagonal moves
    elif (board[0][0] == board[1][1] == board[2][2]):
        winStatus = True
    elif (board[0][2] == board[1][1] == board[2][0]):
        winStatus = True

    return winStatus

def makeMove():
    """
        Combines the above functions to simulate the players move pattern
    """
    board = [[1,2,3],[4,5,6],[7,8,9]]
    count = 0
    win = False
    printBoard(board)
    while (count != 9):

        move = inputPosition()
        moveStatus = checkMove(move)
        if (moveStatus) and (count % 2 == 0):
            currentBoard,status = boardFunc(board,move,"X") 
            printBoard(currentBoard)
            win = winCheck(currentBoard)
            count += 1
            if win:
                print("Player 1 Won!")
                break
        elif (moveStatus) and (count % 2 != 0):
            currentBoard,status = boardFunc(board,move,"O") 
            printBoard(currentBoard)
            win = winCheck(currentBoard)
            count += 1
            if win:
                print("Player 2 Won!")
                break
    if win == False:
        print("Game ended in a Draw!")

def ticTacToe():
    """ Simulates Tic Tac Toe game
        Note: Player 1 is always X and player 2 is always O
    """

    play = 'y'


    while play.lower() == "y":
        
        print("Tic Tac Toe Game\n")

        makeMove()

        play = input("Would you like to play again?(y/n)\n")

ticTacToe() # Run game
