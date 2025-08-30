def add(P, Q):
    #adding 2 nos.
    return P+Q

def subtract(P, Q):
    #subbing 2 nos.
    return P-Q 

def multiply(P, Q):
    #mulling 2 nos.
    return P*Q 

def divide(P, Q):
    #divding 2 nos.
    return P/Q 

#Now, Inputs from User
print("Please select the operstion:")
print("a.Add")
print("b.Subtract")
print("c.Multiply")
print("d.Divide")

choice = input("Please enter your choice (a/b/c/d): ")

num_1 = int (input ("Please enter your first number:"))
num_2 = int (input ("Please enter your second number:"))

if choice == "a" :
    print (num_1 , "+" , num_2 , "=" , add(num_1 , num_2))

elif choice == "b" :
    print (num_1 , "-" , num_2 , "=" , subtract(num_1 , num_2))  

elif choice == "c" :
    print (num_1 , "*" , num_2 , "=" , multiply(num_1 , num_2))  

elif choice == "d" :
    print (num_1 , "/" , num_2 , "=" , divide(num_1 , num_2))  

else:
    print("This is an Invalid Input")