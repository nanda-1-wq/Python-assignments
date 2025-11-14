# Question 3: Cocoa Farm Yield Estimator
bags = int(input("Enter number of cocoa bags harvested: "))
price_per_bag = 850
total_income = bags * price_per_bag
if bags > 100:
    total_income +=2000
print(f"Total income : GHC {total_income} (including bonus)")


