# Question 4: Market Women’s Loan Tracker
women_savings = {
  'Akosua': 200,
   'Ama': 150, 
  'Adwoa': 300
}

print("Current Savings:")
for name, amount in women_savings.items():
    print(f"{name}: GHS {amount}")  

name_to_update = input("Enter the name of the woman to update savings: ")
amount_to_add = float(input("Enter new amount to add: "))
if name_to_update in women_savings:
    women_savings[name_to_update] += amount_to_add
    print("Savings updated successfully.")
else:
    print("Name not found in the records.")


print("="*30+ "Updated Savings" +"="*30)    
for name, amount in women_savings.items():
    print(f"{name}: GHC {amount}")