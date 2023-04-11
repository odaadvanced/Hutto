class Budget:
    def __init__(self, amount):
        self.amount = amount
        
    def spend(money):
        self.amount = self.amount - money
        return self.amount
    
    def deposit(money):
        self.amount += money
        return self.amount
    
    def compute(item):
        pass
    
    def transfer(category1, category2, amount):
       '''Transfers a certain amount from category 1 to category 2.'''
       category1 = category1 - amount
       category2 = category2 + amount
       
    def budget_calculations(item, money, total):
        percent = (money/total) * 100
        print(f'You are spending {percent} % of your budget on {item}.')

class Food(Budget):
    pass
    