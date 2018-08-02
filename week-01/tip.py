price = float(input("Enter the price of a meal: "))

tip = round(0.18 * price, 2)

print("An 18% tip would be", tip)
print("The total including tip would be", price + tip)