# Program to check what temperature is suitable for wearing light clothes

# Taking temperature as input
temperature = float(input("Enter the temperature in °C: "))

# Using conditional statements
if temperature >= 25:
    print("It's hot! You can wear light clothes.")
elif 15 <= temperature < 25:
    print("The weather is moderate. You can wear light clothes but carry a jacket just in case.")
else:
    print("It's cold! Better wear warm clothes like a jacket or pullover.")
