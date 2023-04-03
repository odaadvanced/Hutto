class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
    
    def __str__(self):
        return (f"The {self.color} car has {self.mileage:,} miles.")
    
blue = Car("blue", 20000)
red = Car("red", 30000)

print(blue)
print(red)