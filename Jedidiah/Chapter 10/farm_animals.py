class Animals:
    kingdom = "Animalia"
    def __init__(self, name, animal_type, classification, leg_number, weight):
        self.name = name
        self.animal_type = animal_type
        self.classification = classification
        self.leg_number = leg_number
        self.weight = weight
    
    def __str__(self):
        return f"{self.name} is a {self.animal_type} is a {self.classification} that has {self.leg_number} legs and weights about {self.weight} pounds."
    
    def sound(self, noise):
        return f"{self.name} {noise}"
    
    def eat(self, food):
        return f"{self.name} eats {food}"
    
class Chickens(Animals):
    def __init__(self, name, animal_type = "chicken", classification = "bird", leg_number = 2, weight = 5):
        super().__init__(name, animal_type, classification, leg_number, weight)
        
    def sound(self, noise = "clucks"):
        return super().sound(noise)
    
    def eat(self, food = "grass, seeds, and bugs"):
        return super().eat(food)

class Cats(Animals):
    def sound(self, noise = "meows"):
        return super().sound(noise)

    def eat(self, food = "mice"):
        return super().eat(food)
    
class Dogs(Animals):
    def sound(self, noise = "barks"):
        return super().sound(noise)
    
    def eat(self, food = "dog food"):
        return super().eat(food)

class Cows(Animals):
    def sound(self, noise = "moos"):
        return super().sound(noise)
    
    def eat(self, food = "grass and hay"):
        return super().eat(food)

dog = Animals("dog", "Dog", "Mammal", 4, 100)
print(dog)