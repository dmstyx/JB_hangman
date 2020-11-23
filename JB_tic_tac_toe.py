# Populate board with blank spaces
tics = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

# Winning combinations
win_lines = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8],
             [0, 4, 8], [6, 4, 2]]

# count the number of winning combinations exit game loop Truthy
num = 0
game = True

# Iterate through list for X or Y to win
def win(win_lines, tics):
    global num
    global game
    for items in win_lines:
        if tics[items[0]] == tics[items[1]] == tics[items[2]] == 'X':
            num += 1
            game = False
            print("X wins")

        elif tics[items[0]] == tics[items[1]] == tics[items[2]] == 'O':
            num += 1
            game = False
            print("O wins")

    if (tics.count("X") + tics.count("O")) == 9 and num == 0:
        game = False
        print("Draw")
        
# Show game map
def board(tics):

    print(f"""
    ---------
    | {tics[0]} {tics[1]} {tics[2]} |
    | {tics[3]} {tics[4]} {tics[5]} |
    | {tics[6]} {tics[7]} {tics[8]} |
    ---------
    """)
    # game status 
    state = ''.join(tics)
    (win(win_lines, state))
    return game

# Show edited board
board(tics)
#  Enter Xs and Os
while game:
    try:
        x, y = input("Enter the coordinates:").split()
        if x.isdigit() and y.isdigit():
            x = int(x)
            y = int(y)
            if x and y in [1, 2, 3]:
                coords = (x - 1) + (9 - (3 * y))
                if tics[coords] == ' ':
                    tics[coords] = 'X'
                    board(tics)
                    if game == False:
                        break
                    try:
                        x, y = input("Enter the coordinates:").split()
                        if x.isdigit() and y.isdigit():
                            x = int(x)
                            y = int(y)
                            if x and y in [1, 2, 3]:
                                coords = (x - 1) + (9 - (3 * y))
                                if tics[coords] == ' ':
                                    tics[coords] = 'O'
                                    board(tics)
                                else:
                                    print('This cell is occupied! Choose another one!')
                            else:
                                print("Coordinates should be from 1 to 3!")
                        else:
                            print("You should enter numbers!")
                    except:
                        print("You should enter numbers!")
                else:
                    print('This cell is occupied! Choose another one!')
            else:
                print("Coordinates should be from 1 to 3!")
        else:
            print("You should enter numbers!")
    except:
        print("You should enter numbers!")