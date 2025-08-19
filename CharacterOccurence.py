#Take input of a word
string = input("Please enter your own word :")
#Take input of a character
char = input("Please enter your own character :")
i = 0 
count = 0
#Loop will to find the occurence of the character
while(i < len(string)): #String operation
   
   if (string[i] == char): #Condition 1
      count = count + 1
      i = i + 1
      #Display of the result 
      print("The total number og times", char , "has occured =" , count)
      