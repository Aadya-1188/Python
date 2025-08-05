#Take input for the Student that they can attend exam or not
medical_cause=input("did you have a medical cause Y or N :")
#Take input of the atenndence
atten=int(input("enter the attendence of the student :"))
#checking the user input predicting output acoordingly
if medical_cause == "Y" : #checking the condition 1
    print ("You are allowed to give the Exam")
else: 
    if atten>=75: #checking condition 2
        print ("Allowed")
    else: 
        print ("Not Allowed")