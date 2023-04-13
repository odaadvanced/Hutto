class budget:
    def __init__(self, amount):
        self.amount = amount
        
    def spend (self, cost):
        self.amount = self.amount - cost
        print(f"${self.amount} remaining")
    
    def deposit(self, deposit):
        self.amount += deposit
        print(f"${self.amount} have been allocated to this category in total")
    
    def transfer(self, transaction):
        category_1 = input("From what category do you want to withdraw money?")
        category_1_amount = input(f"Enter an integer to represent the amount of money in {category_1}:")
        transfer = int(input(f"How much money do you want to withdraw from {category_1}?"))
        category_2 = input("To what category do you want to transfer funds?")
        category_2_amount = int(input(f"Enter an integer to represent the amount of money in {category_2}"))
        new_category_1_amount = int(category_1_amount) - transfer
        new_category_2_amount = int(category_2_amount) + transfer
        print(f"The category of {category_1} now contains ${new_category_1_amount}")
        print(f"The category of {category_2} now contains ${new_category_2_amount}")
        # 1. no category_1
    
    def percent_of_total_expenses(self, cost_food, cost_clothing, cost_entertainment):
        cost_food = budget_def.food_cost(self, cost_food)
        # cost_food  = original_food - self.amount
        #cost_clothing = origina.... _ self.amount
        cost_clothing = budget_def.clothing_cost(self, cost_clothing)
        cost_entertainment = budget_def.entertainment_cost(self, cost_entertainment)
        total_expenses = int(cost_food) + int(cost_clothing) + int(cost_entertainment)
        category = input("Pick a category of your budget. Are you interested in the cost of food, clothing, or entertainment?")
        if category == 'food':
            expense = cost_food
        elif category == 'clothing':
            expense = cost_clothing
        elif category == 'entertainment':
            expense = cost_entertainment
        percent = expense/total_expenses * 100
        print(f"{percent}% of total expenses spent on {category}")

class food(budget):
    pass
    #def percent_of_total_expenses(self, expenses):
        #cost_food = original_food - 
        
class clothing(budget):
    pass

class entertainment(budget):
    pass