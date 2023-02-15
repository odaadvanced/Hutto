def invest(amount, rate, years):
    for i in range (years):
        amount = amount * (1 + rate)
        print(f"year {i+1}: ${amount:.2f}")
        
prompt1 = input("Enter an initial amount: ")
inputed_amount = float(prompt1)
prompt2 = input("Enter an annual percentage rate: ")
inputed_apr = float(prompt2)
prompt3 = input("Enter a number of years: ")
inputed_years = int(prompt3)

invest(inputed_amount, inputed_apr, inputed_years)

   