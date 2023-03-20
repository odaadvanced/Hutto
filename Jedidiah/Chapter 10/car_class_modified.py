class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
    
    def drive(self, number):
        self.mileage += 100
        
    def __str__(self):
        return (f"The {self.color} car has {self.mileage:,} miles.")
    
blue = Car("Blue", 20000)
red = Car("Red", 30000)
gray = Car("Gray", 0)

print(blue)
print(red)

gray.drive(100)
print(gray.mileage)
