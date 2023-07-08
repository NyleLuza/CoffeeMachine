MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# TODO 1: Create loop to ask for input and to turn off the coffee machine


def checkCoffee(m, coffee):
    if coffee in m.keys():
        return coffee
    elif coffee == "report":
        print("Water:", resources["water"], "ml")
        print("Milk:", resources["milk"], "ml")
        print("Coffee:", resources["coffee"], "g")
        print("Money: $", profit)
        return
    elif coffee == "off":
        print("GoodBye!")
        return
    else:
        print("We do not have this item!")
        return


def resource():
    if resources["water"] < 0 or resources["milk"] < 0 or resources["coffee"] < 0:
        if resources["water"] < 0:
            print("Sorry there isn't enough water!")
            return False
        elif resources["milk"] < 0:
            print("Sorry there isn't enough milk!")
            return False
        elif resources["coffee"] < 0:
            print("Sorry there isn't enough coffee")
            return False
        else:
            return True


def checkResources(bev, prof):
    if bev == "espresso":
        resources["water"] = resources["water"] - MENU["espresso"]["ingredients"]["water"]
        resources["coffee"] = resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"]
        if resource() == False:
            resources["water"] = resources["water"] + MENU["espresso"]["ingredients"]["water"]
            resources["coffee"] = resources["coffee"] + MENU["espresso"]["ingredients"]["coffee"]
            return 0
        prof = MENU["espresso"]["cost"]
        return prof

    if bev == "latte":
        resources["water"] = resources["water"] - MENU["latte"]["ingredients"]["water"]
        resources["coffee"] = resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]
        resources["milk"] = resources["milk"] - MENU["latte"]["ingredients"]["milk"]
        if resource() == False:
            resources["water"] = resources["water"] + MENU["latte"]["ingredients"]["water"]
            resources["coffee"] = resources["coffee"] + MENU["latte"]["ingredients"]["coffee"]
            resources["milk"] = resources["milk"] + MENU["latte"]["ingredients"]["milk"]
            return 0
        prof = MENU["latte"]["cost"]
        return prof

    if bev == "cappuccino":
        resources["water"] = resources["water"] - MENU["cappuccino"]["ingredients"]["water"]
        resources["coffee"] = resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]
        resources["milk"] = resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"]
        if resource() == False:
            resources["water"] = resources["water"] + MENU["cappuccino"]["ingredients"]["water"]
            resources["coffee"] = resources["coffee"] + MENU["cappuccino"]["ingredients"]["coffee"]
            resources["milk"] = resources["milk"] + MENU["cappuccino"]["ingredients"]["milk"]
            return 0
        prof = MENU["latte"]["cost"]
        return prof


def coins(choice):
    quarters = (float)(input("How Many Quarters?: "))
    quartersT = quarters * 0.25
    dimes = (float)(input("How Many Dimes?: "))
    dimesT = dimes * 0.10
    nickels = (float)(input("How Many Nickels?: "))
    nickelsT = nickels * 0.05
    pennies = (float)(input("How Many Pennies?: "))
    penniesT = pennies * 0.01
    total = quartersT + dimesT + nickelsT + penniesT
    if total < MENU[choice]["cost"]:
        print("You do not have enough coins")

    return total


cof = "on"
while cof != "off":
    cof = input("what would you like (espresso/latte/cappuccino): ")
    choice = checkCoffee(MENU, cof)
    if choice != "espresso" and choice != "latte" and choice != "cappuccino":
        continue
    profitCall = checkResources(choice, profit)
    if profitCall == 0:
        continue
    profit += profitCall
    print("Please Insert Coins.")
    change = coins(choice) - MENU[choice]["cost"]
    print("Here is $",format(change,".2f"),"in change")
    print("Here is your", cof, "Enjoy!")
