# Program to count digits in a number using while loop

# Taking input from the user
num = int(input("Enter a number: "))

count = 0
n = num

# Using while loop to count digits
while n > 0:
    n = n // 10   # remove last digit
    count += 1    # increase counter

# Display result
print("The number", num, "has", count, "digits.")
