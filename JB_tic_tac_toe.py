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
win_lines = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [6, 4, 2]]
count = 0
# For X to win, for Y to win and game not finished
def win(win_lines, tics):
  global count
  for items in win_lines:
      if tics[items[0]] == tics[items[1]] == tics[items[2]] == 'X':
          count += 1
          print("X wins")   
      elif tics[items[0]] == tics[items[1]] == tics[items[2]] == 'O':
          count += 1
          print("O wins")

win(win_lines, tics)
print(count)
# Draw condition
if win(win_lines, tics) == None:
  if count > 1 or tics.count("X") - tics.count("0"):
      print("Impossible")
  elif tics.count('X') + tics.count('O') < 9:
      print("Game not finished")
  elif tics.count("X") + tics.count("O") == 9:
      print("Draw")
