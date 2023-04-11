class Budget:
    def __init__(self, food, clothing, entertainment):
        self.food = food
        self.clothing = clothing
        self.entertainment = entertainment
    
    # deposit, withdraw, percent, transfer, compute
    
    def deposit(self, category, deposit):
        if category == 'food':
            return f"There is ${self.food + deposit} in the Food Category."
        elif category == 'clothing':
            return f"There is ${self.clothing + deposit} in the Clothing Category."
        else:
            return f"There is ${self.entertainment + deposit} in the Entertainment Category."
                
    def withdraw(self, category, withdrawal):
        if category == 'food':
            return f"There is ${self.food - withdrawal} in the Food Category."
        elif category == 'clothing':
            return f"There is ${self.clothing - withdrawal} in the Clothing Category."
        else:
            return f"There is ${self.entertainment - withdrawal} in the Entertainment Category."
        
    def compute(self, category):
        if category == 'food':
            return self.food
        elif category == 'clothing':
            return self.clothing
        else:
            return self.entertainment
        
    def percent(self, category):
        total = self.food + self.clothing + self.entertainment
        if category == 'food':
            amount = self.food
        elif category == 'clothing':
            amount = self.clothing
        else:
            amount = self.entertainment
        try:
            percent = str(amount/total*100) + "%"
            return percent
        except ZeroDivisionError:
            return "0%"
        
    def transfer (self, outflow_category, inflow_category, transfer):
        if inflow_category == 'food':
            self.food = self.food + transfer
            if outflow_category == 'clothing':
                self.clothing = self.clothing - transfer
            else:
                self.entertainment = self.entertainment - transfer
            return f"The Food Category now contains ${self.food}."
        elif inflow_category == 'clothing':
            self.clothing = self.clothing + transfer
            if outflow_category == 'food':
                self.food = self.food - transfer
            else:
                self.entertainment = self.entertainment - transfer
            return f"The Clothing Category now contains ${self.clothing}"
        else:
            self.entertainment = self.entertainment + transfer
            if outflow_category == 'food':
                self.food = self.food - transfer
            else:
                self.clothing = self.clothing - transfer
            return f"The Entertainment Category now contains ${self.entertainment}"
        
    
    def __str__(self):
        return f"""There is ${self.food} ({percent(food)}%) in the Food Category.
There is ${self.clothing} ({percent(clothing)}%) in the Clothing Category.
There is ${self.food} ({percent(entertainment)}%) in the Entertainment Category."""

my_budget = Budget(10, 10, 10)
  