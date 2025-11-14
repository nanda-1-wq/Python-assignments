# Question 5 : MTN Mobile Money Transaction

amount = float(input("Enter amount amount to send: "))

if amount <= 100:
    charge = 2
elif amount <= 500:
    charge = 5
else:
    charge = 10 
total_deduction = amount - charge

print("=====Transaction Summary:======")
print(f"Amount send: GHC {amount}")
print(f"Transaction charge: GHC {charge}")
print(f"Receiver will get: GHC {total_deduction}")
