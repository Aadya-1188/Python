#Take input of number of units consumed from the user 
units = int(input("Please enter the number of Units you consumed :"))
#Check conditions of units consumed
#Then calculate amount and surcharge acoordingly
#surcharge is the tax value 
#Check for the units less than 50 
if (units < 50):
    amount = units * 2.60
    surcharge = 25

 #Check for units less that 100
 elif(units <= 100):
    amount = 130 + ((units - 50)* 3.25)
    surcharge = 35

    #Check for units less or equal to 100
 elif(units <= 200):
    amount = 130 + 162.50 +((units - 100)* 5.26)
    surcharge = 45

    #Check for all the cases other than mentioned 
    #When units consumed are more than 200
 else:
    amount = 130 + 162.5 + 526 ((units - 200)* 8.45)
    surcharge = 75
    #Calculate and Display the total electricity bill
    #Total amount = amount + surcharge
     total = amount + surcharge
    print ("\nEectricity Bill = %.2f" %total)