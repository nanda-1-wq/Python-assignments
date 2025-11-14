#Question 2: WAEC Grading System
# Write a program that accepts a student’s score (0–100) and prints the grade:
grade = int(input("Enter the student's score (0-100): "))
if grade > 100 or grade < 0:
  print("Invalid score! Please enter a score between 0 and 100.")
elif grade >= 80 :
  print("A")
elif grade >= 70 : 
  print("B")
elif grade >= 60 :
  print("C")
elif grade >= 50 :
  print("D")
elif grade >= 40:
  print("E")
else :
  print("F")