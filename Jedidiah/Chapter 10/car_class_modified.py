class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
    
    def __str__(self):
        return (f"The {self.color} car has {self.mileage:,} miles.")
    
    def drive(self, number):
        self.mileage += number
       
gray = Car("Gray", 0)

gray.drive(100)
print(gray.mileage)
