# Program to check if the entered character is an alphabet or not

# Taking input from the user
char = input("Enter a character: ")

# Checking if it's an alphabet
if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
    print(char, "is an alphabet.")
else:
    print(char, "is NOT an alphabet.")
