class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
    
    def __str__(self):
        return (f"The {self.color} car has {self.mileage:,} miles.")
    
blue = Car("Blue", 20000)
red = Car("Red", 30000)

print(blue)
print(red)