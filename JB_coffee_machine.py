<<<<<<< HEAD
# start with 
# At the moment, the coffee machine has $550, 400 ml of water, 540 ml of milk, 120 g of coffee beans, and 9 disposable cups.
# read input "buy", "fill", "take"


water_left = 400
milk_left = 540
coffee_left = 120
cups_left = 9
money_left = 550

print(f"""
The coffee machine has:
{water_left} of water
{milk_left} of milk
{coffee_left} of coffee beans
{cups_left} of disposable cups
{money_left} of money
""")

# for buy
# For one espresso, the coffee machine needs 250 ml of water and 16 g of coffee beans. It costs $4.
# For a latte, the coffee machine needs 350 ml of water, 75 ml of milk, and 20 g of coffee beans. It costs $7.
# And for a cappuccino, the coffee machine needs 200 ml of water, 100 ml of milk, and 12 g of coffee. It costs $6


def buy(choice):
    global water_left, milk_left, coffee_left, cups_left, money_left
    if choice == 1:
        water_left -= 250
        coffee_left -= 16
        money_left += 4
        cups_left -= 1

    elif choice == 2:
        water_left -= 350
        milk_left -= 75
        coffee_left -= 20
        money_left += 7
        cups_left -= 1

    elif choice == 3:
        water_left -= 200
        milk_left -= 100
        coffee_left -= 12
        money_left += 6
        cups_left -= 1


# for fill
# ask them how much water, milk, coffee and how many disposable cups they want to add into the coffee machine.
def fill():
    global water_left, milk_left, coffee_left, cups_left, money_left
    water_left += int(input("Write how many ml of water do you want to add:"))
    
    milk_left += int(input("Write how many ml of milk do you want to add:"))

    coffee_left += int(input("Write how many grams of coffee beans do you want to add:"))

    cups_left += int(input("Write how many disposable cups of coffee do you want to add:"))

# for take 
# give all the money that it earned from selling coffee.
def take():
    global money_left
    print(f"I gave you {money_left}.")
    money_left = 0


action = input("Write action (buy, fill, take):")
# Buying using the buy function Example 1
if action == "buy":
    choice = int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:"))
    buy(choice)
# Fill using the fill function Example 2
elif action == "fill":
    fill()
# Take using the take function Example 3
elif action == "take":
    take()


# print the coffee machine's state after that
print(f"""
The coffee machine has:
{water_left} of water
{milk_left} of milk
{coffee_left} of coffee beans
{cups_left} of disposable cups
{money_left} of money
""")
=======
water =int(input('Write how many ml of water the coffee machine has:'))
milk =int(input('Write how many ml of milk the coffee machine has:'))
coffee =int(input('Write how many grams of coffee beans the coffee machine has:'))
cups =int(input('Write how many cups of coffee you will need:'))

water_used = water // 200
milk_used = milk // 50
coffee_used = coffee // 15
max_cups = min([water_used, milk_used, coffee_used])

cups_left = max_cups - cups

if max_cups == cups:
    print("Yes, I can make that amount of coffee")
elif max_cups > cups:
    print(f'Yes, I can make that amount of coffee (and even {cups_left} more than that)')
else:
    print(f"No, I can make only {max_cups} cups of coffee")
>>>>>>> 1f8da33735f3d3dc3b589b6b9a5ad5112ec6c19d
