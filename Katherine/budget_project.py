class budget:
    def __init__(self, food, clothing, entertainment):
        self.food = food
        self.clothing = clothing
        self.entertainment = entertainment
    
    def compute(self, category):
        if category == "food":
            return self.food
        elif category == "clothing":
            return self.clothing
        elif category == "entertainment":
            return self.entertainment

    def spend(self, category, cost):
        if category == "food" and cost <= self.food:
            self.food -= cost
            print(f"${self.food} remaining in {category} and ${cost} spent")
        elif category == "clothing" and cost <= self.clothing:
            self.clothing -= cost
            print(f"${self.clothing} remaining in {category} and ${cost} spent")
        elif category == "entertainment" and cost <= self.entertainment:
            self.entertinament -= entertainment
            print(f"${self.entertainment} remaining in {category} and ${cost} spent")
        else:
            print("That's not legal! :0")
    
    def deposit(self, category, deposit):
        if category == "food":
            self.food += deposit
            print(f"${self.food} is your new balance in {category}. You deposited ${deposit} into {category}")
        elif category == "clothing":
            self.clothing += deposit
            print(f"${self.clothing} is your new balance in {category}. You deposited ${deposit} into {category}")
        elif category == "entertainment":
            self.entertainment =+ deposit
            print(f"${self.entertainment} is your new balance in {category}. You deposited ${deposit} into {category}")
        else:
            print("That's not legal! :0")
    
    def transfer(self, category_withdraw, category_transfer, amount):
        if category_withdraw == "food" and amount <= self.food:
            self.food -= amount
            print(f"${self.food} is your new balance in {category_withdraw}. You withdrew ${amount} from {category_withdraw}")
        elif category_withdraw == "clothing" and amount <= self.clothing:
            self.clothing -= amount
            print(f"${self.clothing} is your new balance in {category_withdraw}. You withdrew ${amount} from {category_withdraw}")
        elif category_withdraw == "entertainment" and amount <= self.entertainment:
            self.entertainment -= amount
            print(f"${self.entertainment} is your new balance in {category_withdraw}. You withdrew ${amount} from {category_withdraw}")
        else:
            print("That's not legal! :0")
        if category_transfer == "food":
            self.food += amount
            print(f"${self.food} is your new balance in {category_transfer}. You transfered ${amount} into {category_transfer}")
        elif category_transfer == "clothing":
            self.clothing += amount
            print(f"${self.clothing} is your new balance in {category_transfer}. You transfered ${amount} into {category_transfer}")
        elif category_transfer == "entertainment":
            self.entertainment += amount
            print(f"${self.entertainment} is your new balance in {category_transfer}. You transfered ${amount} into {category_transfer}")
        else:
            print("Whoops! That's not a category!")
    
    def percent_of_total_expenses(self, category):
        global food_original
        global clothing_original
        global entertainment_original
        food_expense = food_original - self.food
        clothing_expense = clothing_original - self.clothing
        entertainment_expense = entertainment_original - self.entertainment
        total_expenses = food_expense + clothing_expense + entertainment_expense
        if category == "food":
            expense = food_expense
        elif category == "clothing":
            expense = clothing_expense
        elif category == "entertainment":
            expense = entertainment_expense
        else:
            print("That's not legal! :0")
        try:
            percent_of_spending = (expense/total_expenses) * 100
            print(f"{percent_of_spending:.2f}% of your expenses were spent on {category}")
        except ZeroDivisionError:
            print(f"0.00% of your expenses were spent on {category}")

myBudget = budget(40, 100, 140)
food_original = myBudget.food
clothing_original = myBudget.clothing
entertainment_original = myBudget.entertainment