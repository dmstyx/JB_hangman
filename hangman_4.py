# Write your code here
import random
# This is to test gitgu and git status

start = input('Type "play" to play the game, "exit" to quit:')
if start == 'play':

    guess_list = 'python', 'java', 'kotlin', 'javascript'
    guess = random.choice(guess_list)
    hint = "-"*(len(guess))
    guess_set = set(guess)
    answer_set = set()
    guessed_set = set()
    lowercase_english_letter = set("abcdefghijklmnopqrstuvwxyz")
    print(f"""H A N G M A N""")
    i = 0
    while i < 8:
        i += 1
        letter = input(f"""
    {hint}
    Input a letter: """)
        if len(letter) != 1:
            i -= 1
            print("You should input a single letter")
            continue
        if letter not in lowercase_english_letter:
            i -= 1
            print("Please enter a lowercase English letter")
            continue
        if letter in guessed_set:
            i -= 1
            print("You've already guessed this letter")
            continue
        guessed_set.add(letter)
        if letter in answer_set:
            print("No improvements")
        elif letter in guess_set:
            i -= 1
            answer_set.add(letter)
            hint = guess
            for x in guess:
                if x not in answer_set:
                    hint = hint.replace(x, "-")
        else:
            print("That letter doesn't appear in the word")

        if guess_set == answer_set:
            print(f"""You guessed the word {guess}!
    You survived!""")
            break
    else:

        print("You lost!")
elif start == 'exit':
  exit()
else:
  start