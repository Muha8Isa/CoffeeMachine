from menu import MENU, resources, coins, logo


def price(choice):
    print(f"Price is {MENU[choice]['cost']}")


def check(money, choice):
    if money < MENU[choice]['cost']:
        print("Not enough money.")
        return False
    else:
        balance = money - MENU[choice]['cost']
        print(f"you get the change {balance} back")
        print("Enjoy your drink.")
        return True


def res(choice):
    for ingredient, quantity in MENU[choice]["ingredients"].items():
        resources[ingredient] -= quantity


def fill():
    resource = input("What do you want to fill? 'water', 'milk' or 'coffee'? ").lower()
    if resource == "water":
        max = 3000
        unit = "ml"
    elif resource == "milk":
        max = 2000
        unit = "ml"
    elif resource == "coffee":
        max = 500
        unit = "g"
    quantity = int(input(f"How much {resource} do you want to add to the machine? Max capacity is {max} {unit}: "))
    if resource == "water":
        if quantity + resources["water"] > 3000:
            diff = 3000 - resources["water"]
            print(f"Max capacity reached, you can only add {diff} {unit}")
        else:
            resources["water"] += quantity
            print(f"{resource} filled")
    elif resource == "milk":
        if quantity + resources["milk"] > 2000:
            diff = 2000 - resources["milk"]
            print(f"Max capacity reached, you can only add {diff} {unit}")
        else:
            resources["milk"] += quantity
            print(f"{resource} filled")
    elif resource == "coffee":
        if quantity + resources["coffee"] > 500:
            diff = 500 - resources["coffee"]
            print(f"Max capacity reached, you can only add {diff} {unit}")
        else:
            resources["coffee"] += quantity
            print(f"{resource} filled")


def update():
    import time
    print("New customer in 5 seconds...")
    time.sleep(5)
    print(logo)


def prompt(choice):
    if choice == "report":
        print(resources)
    if choice == "fill":
        fill()
    if choice == "espresso":
        if resources["water"] <= MENU["espresso"]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
            return False
        elif resources["coffee"] <= MENU["espresso"]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")
            return False
        else:
            return True

    if choice == "latte":
        if resources["water"] <= MENU["latte"]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
            return False
        elif resources["milk"] <= MENU["latte"]["ingredients"]["milk"]:
            print("Sorry there is not enough milk.")
            return False
        elif resources["coffee"] <= MENU["latte"]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")
            return False
        else:
            return True

    if choice == "cappuccino":
        if resources["water"] <= MENU["cappuccino"]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
            return False
        elif resources["milk"] <= MENU["cappuccino"]["ingredients"]["milk"]:
            print("Sorry there is not enough milk.")
            return False
        elif resources["coffee"] <= MENU["cappuccino"]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")
            return False
        else:
            return True

print(logo)
while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if not prompt(choice):
        continue
    price(choice)
    money = float(input(f"Insert coins {coins}: "))
    if not check(money, choice):
        continue
    res(choice)
    update()
