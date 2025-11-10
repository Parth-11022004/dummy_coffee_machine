### Coffee Machine (Dictionary Version)

This program is a simple coffee machine simulation.  
It uses dictionaries to store coffee types, their ingredients, and prices.  

The user can:

- Order a coffee (espresso, latte, or cappuccino)  
- See the available resources in the machine  
- Add more resources to the machine (for maintenance)  

The program checks if there are enough ingredients and if the user has inserted enough money.  
If both conditions are met, it makes the coffee, updates the resources, and gives change if needed.  
It keeps running until the user chooses to exit.  

---

### Coffee Machine (Class Version)

This is an improved version of the coffee machine program.  
It uses classes and objects to make the code more organized.  

There are two main classes:

- **Coffee**: holds the details of each coffee type (water, milk, coffee, and cost)  
- **CoffeeMachine**: manages the resources, takes orders, handles payments, and makes coffee  

The user can:

- Order a coffee  
- Check the remaining resources  
- Add more ingredients (for the maintainer)  

The program also checks for errors when entering numbers or choices.  
It shows the price list before ordering and does not crash if wrong input is entered.  
