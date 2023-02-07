def invest(amount, rate, years):
    for x in range(1, int(years)+1):
        amount = float(amount) + float(rate) * float(amount)
        print(f"year {x}: ${amount:.2f}")

prompt_1 = "Enter an initial amount: "
amount_1 = input(prompt_1)

prompt_2 = "Enter an annual percentage rate: "
rate_1 = input(prompt_2)

prompt_3 = "Enter a number of years: "
years_1 = input(prompt_3)

result = invest(amount_1, rate_1, years_1)