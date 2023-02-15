amount = float(input("Enter an amount: "))

for num_people in range(2,6):
    print(f"{num_people} people: ${amount / num_people:,.2f} each")