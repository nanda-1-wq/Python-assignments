#Question 7 Fuel Station Calculator
litres = float(input("Enter number of litres: "))
price_per_litre = 12.50
total_cost = litres*price_per_litre
if litres > 50:
  discount = total_cost * 0.05
  total_cost -= discount
  print(f"Discount applied GHC {discount}")

print(f"Litres: {litres}")
print(f"Price per litre: GHC {price_per_litre}")
print(f"Total cost: GHC {total_cost}")


