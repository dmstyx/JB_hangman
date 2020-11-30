import database
import random
import sys

MENU_PROMPT = """
1. Create an account
2. Log into account
0. Exit
"""

def menu():
  connection = database.connect()
  database.create_tables(connection)

  while (user_input := input(MENU_PROMPT)) != "5":
      if user_input == "1":
          prompt_add_new_card(connection)
      elif user_input == "2":
          log_in(connection)
      elif user_input == "3":
          prompt_find_card(connection)
      elif user_input == "4":
          prompt_see_all_cards(connection)
      elif user_input == "0":
          exit_acc()
      else:
          print("Invalid input")

def prompt_add_new_card(connection):

    card_num = random.randint(400000393832089, 400000999999999)
    pin_number = random.randint(1000, 10000)
    card_number = lahn_genarator(card_num)
    number = int(card_number)
    pin = pin_number
    balance = 0
    print(f"""

Your card has been created
Your card number:
{number}
Your card PIN:
{pin}
""")

    database.add_card(connection, number, pin, balance)

def prompt_see_all_cards(connection):
   cards = database.get_all_cards(connection)
   for card in cards:
      print(f"Acc: {card[1]} Pin: {card[2]} - £{card[3]} ")

def prompt_find_card(connection):
    number = input("Enter card number to find: ")
    cards = database.get_card_by_number(connection, number)

    for card in cards:
        print(f"ACC:{card[1]} Pin:{card[2]} - £{card[3]}")

def lahn_genarator(cn):
    list_cn = [int(i) for i in str(cn)]
    nums = []
    for i in range(len(list_cn)):
        if i % 2 == 0:
            nums.append(list_cn[i] * 2)
        else:
            nums.append(list_cn[i])
    total_nums = sum([x - 9 if x > 9 else x for x in nums])
    if total_nums % 10 != 0:
        new_num = 10 - (total_nums % 10)
        list_cn.append(new_num)
    result = list_cn
    if len(result) < 16:
        result.append(0)
    values = ''.join([str(i) for i in result])
    return values

def log_in(connection):
    print()
    number = input("Enter your card number:")
    pin = input("Enter your PIN:")

    cards = database.get_card_by_number(connection, number)

    if cards:
        for card in cards:
            if number == card[1] and pin == card[2]:
                print("You have successfully logged in!")
                logged_in()
        else:
            print("Wrong card number or PIN!")
            menu()
    else:
        print("\nWrong card number or PIN!")
        menu()

def logged_in():
    logged_in = int(input("""1. Balance
2. Log out
0. Exit
"""))
    if logged_in == 1:
        balance()
    elif logged_in == 2:
        print("You have successfully logged out!")
        menu()
    elif logged_in == 0:
      print("Bye")
      exit_acc()

def balance():
  print("Balance:",0)
  logged_in()

def exit_acc():
    print("Bye")
    sys.exit()

menu()
