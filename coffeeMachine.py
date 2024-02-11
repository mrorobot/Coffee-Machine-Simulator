
print("""
             ((((
            ((((
             ))))
          _ .---.
         ( |`---'|
          \|     |
          : .___, :
           `-----'
"""
)
menu = {
    "latte": {
        "ingredient": {
            "milk": 150,
            "water": 100,
            "coffee": 15},
        "money": 150},
    "espresso": {
        "ingredient": {
            "milk": 0,
            "water": 20,
            "coffee": 25},
        "money": 100},
    "cappuccino": {
        "ingredient": {
            "milk": 180,
            "water": 50,
            "coffee": 15},
        "money": 180}
}

resources = {
    "milk": 450,
    "water": 350,
    "coffee": 100
}

profit = 0


def resources_check(drink_ing):
    global resources
    for item in resources:
        if resources[item] < drink_ing[item]:
            print(f"There is not enough {item} to fulfill your order.")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    total = int(input("How many 20 rupee?: ")) * 20
    total += int(input("How many 10 rupee: ")) * 10
    total += int(input("How many 50 rupees?: ")) * 50
    total += int(input("How many 1 rupee?: ")) * 1
    return total


def check_trans(money_received, drink_cost):
    if money_received < drink_cost:
        print("Sorry, you don't have enough funds. Refund is initiated.")
        return False
    return True


is_on = True
while is_on:
    choice = input("What would you like to have? Press 'cappuccino', 'espresso', or 'latte': ")
    drink = menu.get(choice)
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Milk: {resources['milk']} ml")
        print(f"Water: {resources['water']} ml")
        print(f"Coffee: {resources['coffee']} ml")
        print(f"Profit: ${profit}")
    elif resources_check(drink["ingredient"]):
        money_received = process_coins()
        if check_trans(money_received, drink["money"]):
            money_return = money_received - drink["money"]
            profit += drink["money"]
            for item in drink["ingredient"]:
                resources[item] -= drink["ingredient"][item]
            print(f"Here is your {choice}. Enjoy!")
            if money_return > 0:
                print(f"Here is your {money_return}/. in change.")

