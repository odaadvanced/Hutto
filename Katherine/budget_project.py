class budget:
    def __init__(self, food, clothing, entertainment):
        self.food = food
        self.clothing = clothing
        self.entertainment = entertainment
        
    def spend (self, cost):
        self = self - self.cost
        print(self)
    
    def deposit(category, amount):
        self.category += amount
        
    def transfer(category_1, category_2, transfer):
        category_1 += transfer
        category_2 -= transfer
    
    def percent_of_total_expenses(item, spend, total):
        percent = (spend/total) * 100
        print(f"{percent} of total expenses spent on {item}")