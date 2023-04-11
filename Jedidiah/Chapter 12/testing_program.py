class Budget:
    def __init__(self, food, clothing, entertainment):
        self.food = food
        self.clothing = clothing
        self.entertainment = entertainment        
        
    def __str__(self):
        return(f'''Amount for food: ${self.food}
Amount for clothing: ${self.clothing}
Amount for entertainment: ${self.entertainment}''')
        
    def spend(self, category, amount):
        if category == "food":
            self.food = self.food - amount
        elif category == "clothing":
            self.clothing = self.clothing - amount
        else:
            self.entertainment = self.entertainment - amount
        print(f'You spent ${amount} on {category}.')
        
    def deposit(self, category, amount):
        if category == "food":
            self.food += amount
        elif category == "clothing":
            self.clothing += amount
        else:
            self.entertainment += amount
        print(f'You deposited ${amount} for {category}.')
    
    def compute(self, category):
        if category ==1:
            print(f'Food: ${self.food}')
        elif category == 2:
            print(f'Clothing: ${self.clothing}')
        else:
            print(f'Entertainment: ${self.entertainment}')
    
    def transfer(self, transfer_from, transfer_to, amount):
        '''Transfers a certain amount from category 1 to category 2.'''
        if transfer_from == 'food':
            self.food = self.food - amount
            if transfer_to == 'clothing':               
                self.clothing += amount
            else:
                self.entertainment += amount
        elif transfer_from == 'clothing':
            self.clothing = self.clothing - amount
            if transfer_to == 'food':
                self.food += amount
            else:
                self.entertainment += amount                
        else:
            self.entertainment = self.entertainment - amount
            if transfer_to == 'food':
                self.food += amount
            else:
                self.clothing += amount
                
    def budget_calculations(self, category):        
        '''Budget_calculations calculates what percent each item was of the original.'''
        food_spent = food_original
        clothing_spent = clothing_original
        entertainment_spent = entertainment_original
        total_spent = food_spent + clothing_spent + entertainment_spent
        if category == 'food':
            money = food_spent            
        elif category == 'clothing':
            money = clothing_spent
        else:
            money = entertainment_spent
        try:
            percent = (money/total_spent) * 100
            print(f'You are spending {percent}% of your budget on {category}.')
        except ZeroDivisionError:
            print(f'You are spending 0% of your budget on {category}.')
    
    def budget_current_calculations(self, category):
        total_spent = myBudget.food + myBudget.clothing + myBudget.entertainment
        if total_spent > 0:
            if category == "food":
                percent = self.food / total_spent * 100
            elif category == "clothing":
                percent = self.clothing / total_spent * 100
            else:
                percent = self.entertainment / total_spent * 100
            print(f'{percent} % of your budget is for {category}.')
        else:
            print(f'0% of your budget is for {category}.')
            
    def budget_spent_calculations(self, category):
        global food_original
        global clothing_original
        global entertainment_original
        spent_on_food = food_original - self.food
        spent_on_clothing = clothing_original - self.clothing
        spent_on_entertainment = entertainment_original - self.entertainment
        total_spent = spent_on_food + spent_on_clothing + spent_on_entertainment
        if total_spent > 0:
            if category == "food":
                percent = spent_on_food/total_spent * 100
            elif category == "clothing":
                percent = spent_on_clothing/total_spent * 100
            else:
                percent = spent_on_entertainment/total_spent * 100
            print(f'Your spending on {category} is {percent}% of your total spending so far.')
        else:
            print(f'Your spending on {category} is 0% of your total spending so far.')
            
myBudget = Budget(3500, 1000, 500)
food_original = myBudget.food
clothing_original = myBudget.clothing
entertainment_original = myBudget.entertainment