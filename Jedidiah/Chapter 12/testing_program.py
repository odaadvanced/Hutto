spent_for_food = 0
spent_for_clothing = 0
spent_for_entertainment = 0

class Budget:
    def __init__(self, food, clothing, entertainment):
        self.food = food
        self.clothing = clothing
        self.entertainment = entertainment        
        
    def __str__(self):
        return(f'''Amount for food: ${self.food}
Amount for clothing: ${self.clothing}
Amount for entertainment: ${self.entertainment}''')
        
    def spend(self, category1, category2, category3):
        global spent_for_food
        global spent_for_clothing
        global spent_for_entertainment
        self.food = self.food - category1
        self.clothing = self.clothing - category2
        self.entertainment = self.entertainment - category3
        spent_for_food += category1
        spent_for_clothing += category2
        spent_for_entertainment += category3
        print(f'''You spent ${category1} on food, ${category2} on clothing,
and ${category3} on entertainment.''')
        return (spent_for_food, spent_for_clothing, spent_for_entertainment)
 
    def deposit(self, category1, category2, category3):
        self.food += category1
        self.clothing += category2
        self.entertainment += category3
        print(f'''You deposited ${category1} for food, ${category2} for
clothing, and ${category3} for entertainment.''')
    
    def compute(self, category):
        if category ==1:
            print(f'Food: ${self.food}')
        elif category == 2:
            print(f'Clothing: ${self.clothing}')
        else:
            print(f'Entertainment: ${self.entertainment}')
    
    def transfer(self, transfer_from, transfer_to, amount):
        '''Transfers a certain amount from category 1 to category 2.'''
        if transfer_from == 1:
            self.food = self.food - amount
            if transfer_to == 2:               
                self.clothing += amount
            else:
                self.entertainment += amount
        elif transfer_from == 2:
            self.clothing = self.clothing - amount
            if transfer_to == 1:
                self.food += amount
            else:
                self.entertainment += amount                
        else:
            self.entertainment = self.entertainment - amount
            if trannsfer_to ==1:
                self.food += amount
            else:
                self.clothing += amount
                
    def budget_calculations(self, category):        
        food_spent = spend[0]
        clothing_spent = spend[1]
        entertainment_spent = spend[2]
        total_spent = food_spent + clothing_spent + entertainment_spent
        if category == 1:
            money = food_spent
            category_from = food
        elif category == 2:
            money = clothing_spent
            category_from = clothing
        else:
            money = entertainment_spent
            category_from = entertainment 
        percent = (money/total_spent) * 100
        print(f'You are spending {percent} % of your budget on {category_from}.')

myBudget = Budget(3500, 1000, 500)