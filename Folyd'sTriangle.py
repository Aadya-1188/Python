#Take input form user
rows = int(input("Enter the nom. of rows:"))
number = 1 #initialise by 1

print("Floyd's Triangle")
#Outer loop for number of rows

for i in range (1, rows + 1):

#Inner loop for number of columns

   for j in range(1,i + 1):
  
#Display Result

      print(number, end="")
      number = number + 1
   print()