food = ["rice", "beans"]
food.append("broccoli")
food.extend(["bread", "pizza"])
print(food[0:2])
print(food[-1:])
breakfast_foods = "eggs, fruit, orange juice"
breakfast =  breakfast_foods.split(", ")
num_of_foods = len(breakfast)
lengths = [len(foods) for foods in breakfast]