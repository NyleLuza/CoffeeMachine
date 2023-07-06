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

#TODO 1: Create loop to ask for input and to turn off the coffee machine

cof = input("what would you like (espresso/latte/cappuccino): ")

def checkCoffee(m, coffee):
    if coffee in m.keys():
        return coffee
    elif coffee == "report":
        print(str(resources))
        return
    else:
        cof = input("what would you like (espresso/latte/cappuccino): ")
        return cof

def checkResources(bev):
    if(bev == "espresso"):
        resources["water"] = resources["water"] - MENU["espresso"]["ingredients"]["water"]
        resources["coffee"] = resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"]

    if(bev == "latte"):
        resources["water"] = resources["water"] - MENU["latte"]["ingredients"]["water"]
        resources["coffee"] = resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]
        resources["milk"] = resources["milk"] - MENU["latte"]["ingredients"]["milk"]

    if (bev == "cappuccino"):
        resources["water"] = resources["water"] - MENU["cappuccino"]["ingredients"]["water"]
        resources["coffee"] = resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]
        resources["milk"] = resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"]

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
    if(total<MENU[choice]["cost"]):
        print("You do not have enough coins")
    elif(total>MENU[choice]["cost"]):
        change = total-MENU[choice]["cost"]
        print("Here is your change ",change)

    return total
while cof!= "off":
    choice = checkCoffee(MENU, cof)
    print("Please Insert Coins.")
    total = coins(choice)
    print(total)
    profit += MENU[choice]["cost"]
    print(profit)
    cof = input("what would you like (espresso/latte/cappuccino): ")

