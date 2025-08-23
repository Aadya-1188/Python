# Program to check if age is between 10 and 20 using nested conditional statements

age = int(input("Enter your age: "))

if age >= 10:
    if age <= 20:
        print("Yes ✅ The age is between 10 and 20.")
    else:
        print("No ❌ The age is greater than 20.")
else:
    print("No ❌ The age is less than 10.")
