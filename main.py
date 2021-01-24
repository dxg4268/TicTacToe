game_input = ['Default','-','-','-','-','-','-','-','-','-']
winner = None
game_running = True
# print(type(game_input))

# ----------------Functions----------------
def gameBoard():
    print(game_input[7] + "  |  " + game_input[8] + "  |  " + game_input[9] + "\t\t7  |  8  |  9")
    print("-------------")
    print(game_input[4] + "  |  " + game_input[5] + "  |  " + game_input[6] + "\t\t4  |  5  |  6")
    print("-------------")
    print(game_input[1] + "  |  " + game_input[2] + "  |  " + game_input[3] + "\t\t1  |  2  |  3")
    

def Player1(num):
    if game_input[num] == '-':
        game_input[num] = 'X'
    else:
        print("You cannot come here... Try Again")
        # valid = False
        while True:
            num = int(input("Enter position of X  : "))
            if game_input[num] == '-':
                game_input[num] = 'X'
                break
            else:
                continue
         

def Player2(num):
    if game_input[num] == '-':
        game_input[num] = 'O'
    else:
        print("You cannot come here... Try Again")
        # valid = False
        while True:
            num = int(input("Enter position of O  : "))
            if game_input[num] == '-':
                game_input[num] = 'O'
                break
            else:
                continue


def checkGameOver():
    win()
    gameTie()


def win():
    global winner
    row_winner = check_rows()
    diag_winner = check_diagonals()
    col_winner = check_columns()

    if row_winner:
        winner = row_winner
    elif diag_winner:
        winner = diag_winner
    elif col_winner:
        winner = col_winner
    else:
        winner = None

def check_rows():
    global game_running
    # winner = None
    row1 = game_input[7] == game_input[8] == game_input[9] != '-'
    row2 = game_input[4] == game_input[5] == game_input[6] != '-'
    row3 = game_input[1] == game_input[2] == game_input[3] != '-'

    if row1 or row2 or row3:
        game_running = False
    if row1:
        return game_input[7]
    elif row2:
        return game_input[4]
    elif row3:
        return game_input[1]
    else:
        return None


def check_columns():
    global game_running

    col1 = game_input[7] == game_input[4] == game_input[1] != '-'
    col2 = game_input[8] == game_input[5] == game_input[2] != '-'
    col3 = game_input[9] == game_input[6] == game_input[3] != '-'

    if col1 or col2 or col3:
        game_running = False

    if col1:
        return game_input[7]
    elif col2:
        return game_input[8]
    elif col3:
        return game_input[9]
    else:
        return None
    


def check_diagonals():
    global game_running

    diagonal_1 = game_input[7] == game_input[5] == game_input[3] != '-'
    diagonal_2 = game_input[9] == game_input[5] == game_input[1] != '-'

    if diagonal_1 or diagonal_2:
        game_running = False

    if diagonal_1:
        return game_input[7]
    elif diagonal_2:
        return game_input[9]
    else:
        return None


def gameTie():
    global game_running

    if '-' not in game_input:
        game_running = False
        return True
    else:
        return False


def playGame():
    global game_running
    # game_running = True
    while game_running:
        gameBoard()

        prompt_msg = "Enter Position of Player1 : "
        num = int(input(prompt_msg))
        Player1(num)
        gameBoard()

        checkGameOver()
        if game_running == False:
            break
        print("\n")
        prompt_msg = "Enter Position of Player2 : "
        num = int(input(prompt_msg))
        Player2(num)
        gameBoard()

        print("\n\n")

        checkGameOver()

    if winner == "X" or winner == "O":
        print("\nCongratulations! Winner is " + winner)
    elif winner == None:
        print("Tie")



# ------------------Start Execution of the program----------------------
playGame()

