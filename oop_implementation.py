class Coffee:
    def __init__(self, water, milk, coffee, cost):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cost = cost

espresso = Coffee(50,18,0,100)
latte = Coffee(208,150,24,200)
cappuccino = Coffee(250,100,24,250)

coffee_dict = {
    1 : espresso,
    2 : latte,
    3 : cappuccino
}

class Coffee_machine:
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
            "money": 5000
        }

    def print_resources(self):
        print("Available resources:")
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")
        print(f"Money: {self.resources['money']}₹")
    
    def add_resources(self):
        for i in self.resources:
            amount = int(input(f"add {i} amount: "))
            self.resources[i] += amount
        print("resources have been added successfully")

    def coffee_choice(self):
        while True:
            choice = int(input("""What would you like?
                                Espresso: press 1
                                Latte: press 2
                                Cappuccino: press 3\n"""))
            if choice not in [1,2,3]:
                print('enter a valid choice')
                continue
            return choice
    
    def check_resources_sufficient(self, coffee_type):
            if self.resources['water'] < coffee_dict[coffee_type].water:
                print('not enough water')
                return False
            elif self.resources['milk'] < coffee_dict[coffee_type].milk:
                print('not enough milk')
                return False
            elif self.resources['coffee'] < coffee_dict[coffee_type].coffee:
                print('not enough coffee')
                return False
            else:
                return True

    def enter_money(self):
        user_money = int(input("Enter money: "))
        return user_money
        
    def check_money_sufficient(self, user_money, coffee_type):
        if user_money >= coffee_dict[coffee_type].cost:
            change = user_money - coffee_dict[coffee_type].cost
            print(f"Here's your change: {change}, Enjoy!")
            return True
        else:
            print("sorry, not enough money was entered")
            return False   
         
    def update_resources(self, coffee_type):
        self.resources['water'] -= coffee_dict[coffee_type].water
        self.resources['milk'] -= coffee_dict[coffee_type].milk
        self.resources['coffee'] -= coffee_dict[coffee_type].coffee
        self.resources['money'] += coffee_dict[coffee_type].cost

machine1 = Coffee_machine()

while True:
    x = int(input("""Welcome to the coffee machine, what would you like to do?
            order coffee: press 1
            see available resources: press 2
            add resources to machine: press 3\n""")) # only for maintainer
    if x == 1:
        coffee_choice = machine1.coffee_choice()
        suff_or_not = machine1.check_resources_sufficient(coffee_choice)
        if suff_or_not == True:
            user_money = machine1.enter_money()
            to_update = machine1.check_money_sufficient(user_money, coffee_choice)
            if to_update == True:
                machine1.update_resources(coffee_choice)
    elif x == 2:
        machine1.print_resources()
    elif x == 3:
        machine1.add_resources()
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


