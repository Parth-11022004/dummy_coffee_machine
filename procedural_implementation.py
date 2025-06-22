menu  = {
"espresso": {
    "ingredients": {
        "water": 50,
        "coffee": 18
        },
    "cost": 100
},    
"latte": {
    "ingredients": {
        "water": 208,
        "milk": 150,
        "coffee": 24
        },
    "cost": 200
},
"cappuccino": {
    "ingredients": {
        "water": 250,
        "milk": 100,
        "coffee": 24
    },
    "cost": 250
}
}
resources = {
    "water": 300, 
    "milk": 200,
    "coffee":180,
    "money":5000
}
def print_resources():
    print(f"""Available resources:
          water: {resources['water']}
          milk: {resources['milk']}
          coffee: {resources['coffee']}
          money: {resources['money']}""")
    
def add_resources(water: float, milk: float, coffee: float, money: float):
    resources["water"] += water
    resources["milk"] += milk
    resources["coffee"] += coffee
    resources["money"] += money
    print("resources have been added to the coffee machine successfully.")

def coffee():
    while True:
        coffee_choice = int(input("""What would you like?
                 espresso: press 1
                 latte: press 2
                 cappuccino: press 3\n""")) 
        if coffee_choice == 1:
            if resources["water"] < menu["espresso"]["ingredients"]["water"] or resources["coffee"] < menu["espresso"]["ingredients"]["coffee"]:
                print("sorry not enough resources")
            else:
                resources["water"] -= menu["espresso"]["ingredients"]["water"]
                resources["coffee"] -= menu["espresso"]["ingredients"]["coffee"]
                user_money = int(input("insert money: "))
                if user_money >= menu["espresso"]["cost"]:
                    resources["money"] += menu["espresso"]["cost"]
                    change = user_money - menu["espresso"]["cost"]
                    print(f"here's your change: {change}")
                    print("Enjoy your coffee!")
                else:
                    print("sorry, not enough money was inserted")
        
        elif coffee_choice == 2:
            if resources["water"] < menu["latte"]["ingredients"]["water"] or resources["coffee"] < menu["latte"]["ingredients"]["coffee"] or resources["milk"] < menu["latte"]["ingredients"]["milk"]:
                print("sorry not enough resources")
            else:
                resources["water"] -= menu["latte"]["ingredients"]["water"]
                resources["coffee"] -= menu["latte"]["ingredients"]["coffee"]
                resources["milk"] -= menu["latte"]["ingredients"]["milk"]
                user_money = int(input("insert money: "))
                if user_money >= menu["latte"]["cost"]:
                    resources["money"] += menu["latte"]["cost"]
                    change = user_money - menu["latte"]["cost"]
                    print(f"here's your change: {change}")
                    print("Enjoy your coffee!")
                else:
                    print("sorry, not enough money was inserted")
        
        elif coffee_choice == 3:
            if resources["water"] < menu["cappuccino"]["ingredients"]["water"] or resources["coffee"] < menu["cappuccino"]["ingredients"]["coffee"] or resources["milk"] < menu["cappuccino"]["ingredients"]["milk"]:
                print("sorry not enough resources")
            else:
                resources["water"] -= menu["cappuccino"]["ingredients"]["water"]
                resources["coffee"] -= menu["cappuccino"]["ingredients"]["coffee"]
                resources["milk"] -= menu["cappuccino"]["ingredients"]["milk"]
                user_money = int(input("insert money: "))
                if user_money >= menu["cappuccino"]["cost"]:
                    resources["money"] += menu["cappuccino"]["cost"]
                    change = user_money - menu["cappuccino"]["cost"]
                    print(f"here's your change: {change}")
                    print("Enjoy your coffee!")
                else:
                    print("sorry, not enough money was inserted")
        
        else:
            print("enter a valid choice")
            continue
        
        order_again = int(input("""Would you like to order again?
                                   Yes: press 1
                                   No: press 0\n"""))
        if order_again == 1:
            continue
        else:
            break

while True:
    x = int(input("""Welcome to the coffee machine, what would you like to do?
            order coffee: press 1
            see available resources: press 2
            add resources to machine: press 3\n""")) # only for maintainer
    if x == 1:
        coffee()
    elif x == 2:
        print_resources()
    elif x == 3:
        water_amount = int(input("enter water amount: "))
        milk_amount = int(input("enter milk amount: "))
        coffee_amount = int(input("enter coffee amount: "))
        money_amount = int(input("enter money: "))
        add_resources(water_amount, milk_amount, coffee_amount, money_amount)
    else:
        print('enter a valid choice')
        continue    
    use_again = int(input("""would you like to use the machine again?
                             Yes: press 1
                             No: press 0\n"""))
    if use_again == 1:
        continue
    else:
        break
    
