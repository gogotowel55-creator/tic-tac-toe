#Project: Tic Tac Toe

#Creating a Board

board = []
for i in range(9):
    board.append(" ")

#Function to Print Board

def print_board():
    print()
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")

#Function to Check Winner

def check_winner(current_player):
    #Row One
    if current_player == board[0] == board[1] == board[2]:
        return True
    #Row Two
    if current_player == board[3] == board[4] == board[5]:
        return True
    #Row Three
    if current_player == board[6] == board[7] == board[8]:
        return True
    #Column One
    if current_player == board[0] == board[3] == board[6]:
        return True
    #Column Two
    if current_player == board[1] == board[4] == board[7]:
        return True
    #Column Three
    if current_player == board[2] == board[5] == board[8]:
        return True
    #Diagonal One
    if current_player == board[0] == board[4] == board[8]:
        return True
    #Diagonal Two
    if current_player == board[2] == board[4] == board[6]:
        return True
    #Tie
    return False

#Two Player Game

def game():
    current_player = 'x'
    space_occupied = 0
    #for turn in range(9):
    #For loop for adding restriction to 9 attempts only
    #While loop for more flexibility of play, allowing infinite play until there is a winner or the board is full.
    while space_occupied != 9:
        print_board()
        position = int(input(f"{current_player}, please enter where you want to move (1-9)"))-1
        if board[position] != " ":
            print("Sorry, this space is already taken. Please try again.")
            continue
        else:
            board[position] = current_player
            space_occupied += 1
            winner = check_winner(current_player)
            if winner == True:
                print_board()
                print(f"Hooray, {current_player}! You won!")
                return
            else:
                if current_player == "x":
                    current_player = "o"
                else:
                    current_player = "x"
    print_board()
    print("It's a tie!")

game()
    
        
        
        

