class Budget:
    def __init__(self, amount):
        self.amount = amount
        
    def spend(self, money):
        self.amount = self.amount - money
        return self.amount
    
    def deposit(self, money):
        self.amount += money
        return self.amount
    
    def compute(self, item):
        return self.amount
    
    def transfer(self, category, amount):
       '''Transfers a certain amount from category 1 to category 2.'''
       self.amount = self.amount - amount
       category += amount
       
    def budget_calculations(self, money, total):
        percent = (money/total) * 100
        print(f'You are spending {percent} % of your budget on {item}.')

food = Budget(3500)
clothing = Budget(1000)
entertainment = Budget(500)

    