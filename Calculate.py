
# Program to calculate the power of a number using for loop

# Taking input from the user
base = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent (power): "))

result = 1

# Using for loop to calculate power
for i in range(exponent):
    result *= base

# Display result
print(base, "raised to the power of", exponent, "is:", result)
