# Program to convert decimal number to binary using while loop

# Taking input from the user
decimal = int(input("Enter a decimal number: "))

binary = ""   # to store binary digits
num = decimal

# Using while loop to convert
while num > 0:
    remainder = num % 2
    binary = str(remainder) + binary
    num = num // 2

# Display result
print("The binary of", decimal, "is:", binary)
