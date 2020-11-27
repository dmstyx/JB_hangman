# JetBrains banking app
import random

# dictionary for all the users, cards and pins
user = {}

# main menu at start-up

def main_menu():
    start = int(input("""1. Create an account
2. Log into account
0. Exit   
"""))
    if start == 1:
      create_account()
    elif start == 2:
      log_in()
    elif start == 0:
      exit_acc()

# create random account number and pin
def create_account():

    card_number = random.randint(400000393832089, 400000999999999)
    pin_number = random.randint(1000, 10000)
    
    user["card_number"] = card_number
    user["pin_number"] = pin_number
    print(f"""

Your card has been created
Your card number:
{card_number}
Your card PIN:
{pin_number}
""")
# return to main menu
    main_menu()

# log in usings new details 
def log_in():
    print()
    card = int(input("Enter your card number:"))
    pin = int(input("Enter your PIN:"))
    if card == user["card_number"] and pin == user["pin_number"]:
        print("You have successfully logged in!")
        logged_in()
    else:
        print("Wrong card number or PIN!")
        main_menu()

# logged in menu
def logged_in():
        logged_in = int(input("""1. Balance
2. Log out
0. Exit
"""))
        if logged_in == 1:
            balance()
        elif logged_in == 2:
            print("You have successfully logged out!")
            main_menu()

# show balance
def balance():
    print("Balance:",0)
    logged_in()

#  quit
def exit_acc():
    exit()

def lahn_checker(cn):

    list_cn = [int(i) for i in str(cn)]
    check_sum = list_cn.pop()
    nums = []
    for i in range(len(list_cn)):
        if i % 2 == 0:
            nums.append(list_cn[i] * 2)
        else:
            nums.append(list_cn[i])
    total_nums = check_sum + sum([x - 9 if x > 9 else x for x in nums]) 

    print(total_nums)

def lahn_genarator(cn):
    list_cn = [int(i) for i in str(cn)]
    nums = []
    for i in range(len(list_cn)):
        if i % 2 == 0:
            nums.append(list_cn[i] * 2)
        else:
            nums.append(list_cn[i])
    total_nums = sum([x - 9 if x > 9 else x for x in nums]) 
    new_num = 10 - (total_nums % 10)
    list_cn.append(new_num)

    print(total_nums + new_num)
    print(list_cn)


main_menu()

