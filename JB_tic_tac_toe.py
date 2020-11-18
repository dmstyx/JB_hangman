tics = list(input())

# Show game map
print(f"""
---------
| {tics[0]} {tics[1]} {tics[2]} |
| {tics[3]} {tics[4]} {tics[5]} |
| {tics[6]} {tics[7]} {tics[8]} |
---------
""")

# Winning combinations
win_lines = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8],
             [0, 4, 8], [6, 4, 2]]

# count the number of winning combinations
num = 0

# Iterate through list for X or Y to win
def win(win_lines, tics):
    global num  
    for items in win_lines:
        if tics[items[0]] == tics[items[1]] == tics[items[2]] == 'X':
            num += 1
            print("X wins")
        elif tics[items[0]] == tics[items[1]] == tics[items[2]] == 'O':
            num += 1
            print("O wins")

# Show winner
win(win_lines, tics)

# DNF conditions
if abs(tics.count("X") - tics.count("O")) > 1:
    print("Impossible")
elif num > 1:
    print("Impossible")
elif num == 0 and (tics.count("X") + tics.count("O") < 9):
    print("Game not finished")
elif (tics.count("X") + tics.count("O")) and num == 0 and win(win_lines, tics) == None:
    print("Draw")



    # while True:
    # x , y = input("Enter the coordinates:").split()
    # if x.isdigit() and y.isdigit():
    #     if int(x) and int(y) in [1,2,3]:
    #         print("All good")
    #         break
    #     else:
    #         print("Coordinates should be from 1 to 3!")
    # else:
    #     print("You should enter numbers!")