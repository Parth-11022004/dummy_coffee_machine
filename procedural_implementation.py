menu = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18},
        "cost": 100
    },
    "latte": {
        "ingredients": {"water": 208, "milk": 150, "coffee": 24},
        "cost": 200
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 250
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 180,
    "money": 5000
}


def print_menu():
    print("\n☕ Coffee Menu (in Rs):")
    for item, info in menu.items():
        print(f" - {item.title():12} : Rs {info['cost']}")
    print()


def print_resources():
    print(f"""
📦 Available Resources:
  Water : {resources['water']} ml
  Milk  : {resources['milk']} ml
  Coffee: {resources['coffee']} g
  Money : Rs {resources['money']}
""")


def add_resources():
    try:
        water = int(input("Enter water amount to add (ml): "))
        milk = int(input("Enter milk amount to add (ml): "))
        coffee = int(input("Enter coffee amount to add (g): "))
        money = int(input("Enter money to add (Rs): "))
    except ValueError:
        print("❌ Invalid input! Please enter numeric values only.")
        return

    resources["water"] += water
    resources["milk"] += milk
    resources["coffee"] += coffee
    resources["money"] += money
    print("✅ Resources have been added successfully.")


def make_coffee(choice):
    drink = menu[choice]
    ingredients = drink["ingredients"]

    # Check for sufficient resources
    for item in ingredients:
        if resources[item] < ingredients[item]:
            print(f"❌ Sorry, not enough {item}.")
            return

    # Ask for payment
    try:
        user_money = int(input("Insert money (Rs): "))
    except ValueError:
        print("❌ Invalid input! Please insert numeric value.")
        return

    if user_money < drink["cost"]:
        print("❌ Sorry, not enough money was inserted.")
        return

    # Deduct ingredients
    for item in ingredients:
        resources[item] -= ingredients[item]

    resources["money"] += drink["cost"]
    change = user_money - drink["cost"]
    print(f"✅ Enjoy your {choice}! ☕ Your change: Rs {change}")


def coffee():
    print_menu()
    while True:
        try:
            coffee_choice = int(input("""
What would you like?
  1 - Espresso
  2 - Latte
  3 - Cappuccino
Choice: """))
        except ValueError:
            print("❌ Invalid input! Please enter 1, 2, or 3.")
            continue

        options = {1: "espresso", 2: "latte", 3: "cappuccino"}

        if coffee_choice in options:
            make_coffee(options[coffee_choice])
        else:
            print("❌ Invalid choice. Please try again.")
            continue

        again = input("\nWould you like to order again? (y/n): ").strip().lower()
        if again != 'y':
            break


# --- Main Loop ---
while True:
    print_menu()
    try:
        x = int(input("""
Welcome to the Coffee Machine! What would you like to do?
  1 - Order coffee
  2 - See available resources
  3 - Add resources (maintainer only)
Choice: """))
    except ValueError:
        print("❌ Invalid input! Please enter a number (1–3).")
        continue

    if x == 1:
        coffee()
    elif x == 2:
        print_resources()
    elif x == 3:
        add_resources()
    else:
        print("❌ Enter a valid choice (1–3).")
        continue

    again = input("\nWould you like to use the machine again? (y/n): ").strip().lower()
    if again != 'y':
        print("👋 Goodbye! Have a nice day!")
        break
