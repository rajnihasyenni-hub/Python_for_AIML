principal = float(input("Enter Principal amount: "))
rate = float(input("Enter Annual Interest Rate (%): "))
for year in range(1, 6):
    amount = principal * (1 + rate/100) ** year
    print("Balance at end of Year", year, "=", round(amount, 2))
