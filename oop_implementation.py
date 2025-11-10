class Coffee:
    def __init__(self, water, milk, coffee, cost):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cost = cost


espresso = Coffee(50, 0, 18, 100)
latte = Coffee(208, 150, 24, 200)
cappuccino = Coffee(250, 100, 24, 250)

coffee_dict = {
    1: espresso,
    2: latte,
    3: cappuccino
}


# ---------- Utility Safe Input Function ----------
def safe_int_input(prompt, valid_values=None):
    while True:
        try:
            value = int(input(prompt))
            if valid_values and value not in valid_values:
                print("❌ Invalid choice! Try again.")
                continue
            return value
        except ValueError:
            print("❌ Please enter a valid number.")


# ---------- Coffee Machine Class ----------
class CoffeeMachine:
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
            "money": 5000
        }

    def print_resources(self):
        print("\n📦 Available Resources:")
        print(f"Water : {self.resources['water']} ml")
        print(f"Milk  : {self.resources['milk']} ml")
        print(f"Coffee: {self.resources['coffee']} g")
        print(f"Money : ₹{self.resources['money']}\n")

    def add_resources(self):
        print("\n🔧 Add Resources (for maintainer):")
        for key in ["water", "milk", "coffee"]:
            amount = safe_int_input(f"Add {key} amount: ")
            self.resources[key] += amount
        print("✅ Resources have been added successfully.\n")

    def show_menu(self):
        print("\n☕ Coffee Menu:")
        print("1. Espresso (₹100)")
        print("2. Latte (₹200)")
        print("3. Cappuccino (₹250)\n")

    def coffee_choice(self):
        self.show_menu()
        choice = safe_int_input("Select your drink (1–3): ", [1, 2, 3])
        return choice

    def check_resources_sufficient(self, coffee_type):
        drink = coffee_dict[coffee_type]
        if self.resources["water"] < drink.water:
            print("❌ Not enough water.")
            return False
        if self.resources["milk"] < drink.milk:
            print("❌ Not enough milk.")
            return False
        if self.resources["coffee"] < drink.coffee:
            print("❌ Not enough coffee.")
            return False
        return True

    def enter_money(self):
        user_money = safe_int_input("💰 Insert money (₹): ")
        return user_money

    def check_money_sufficient(self, user_money, coffee_type):
        drink = coffee_dict[coffee_type]
        if user_money >= drink.cost:
            change = user_money - drink.cost
            print(f"✅ Here's your change: ₹{change}")
            print("☕ Enjoy your coffee!\n")
            return True
        else:
            print("❌ Sorry, not enough money was entered.\n")
            return False

    def update_resources(self, coffee_type):
        drink = coffee_dict[coffee_type]
        self.resources["water"] -= drink.water
        self.resources["milk"] -= drink.milk
        self.resources["coffee"] -= drink.coffee
        self.resources["money"] += drink.cost


# ---------- Main Program ----------
machine1 = CoffeeMachine()

while True:
    print("\n========= COFFEE MACHINE =========")
    print("1. Order Coffee")
    print("2. See Available Resources")
    print("3. Add Resources (maintainer only)")
    print("==================================")

    x = safe_int_input("Enter your choice (1–3): ", [1, 2, 3])

    if x == 1:
        choice = machine1.coffee_choice()
        if machine1.check_resources_sufficient(choice):
            money = machine1.enter_money()
            if machine1.check_money_sufficient(money, choice):
                machine1.update_resources(choice)
                print(f"✅ Dispensing your {['Espresso', 'Latte', 'Cappuccino'][choice-1]}...\n")
    elif x == 2:
        machine1.print_resources()
    elif x == 3:
        machine1.add_resources()

    again = input("Would you like to use the machine again? (y/n): ").strip().lower()
    if again != "y":
        print("\n👋 Thank you for using the Coffee Machine. Goodbye!")
        break
