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