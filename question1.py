#Question1 
# TorTor Fare Calculator
print("Welcome to the TorTor Fare Calculator")
user = int(input("""Please Select  your route;
1. Accra -> Madina = GHC 5.
2. Accra -> Kasoa= GHC 10.
3. Accra -> Tema = GHC 8.
Enter 1, 2,or 3: """))
number_of_passengers = int(input("How many passengers are you loading? "))
if user == 1:
  fare_per_passenger = 5
  total_fare = fare_per_passenger * number_of_passengers
  print(f"Total fare for {number_of_passengers} passengers from Accra to Madina is GHC {total_fare}.")
elif user == 2:
  fare_per_passenger = 10
  total_fare = fare_per_passenger * number_of_passengers
  print(f"Total fare for {number_of_passengers} Passengers from Accra to Kasoa is GHC {total_fare}.")
elif user == 3:
  fare_per_passenger = 8
  total_fare = fare_per_passenger * number_of_passengers
  print(f"Total fare for {number_of_passengers} Passengers from Accra to Tema is GHC {total_fare}.")
else:
  print("Invalid route selection. Please enter 1, 2, or 3.")
 


