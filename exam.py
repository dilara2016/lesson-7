#Take input for the student that he can atend the exam or not
medical_cause=input("did you have a medical cause Y or N")
#Take input of attendance
atten = int(input("enter the attendance for student: "))
#checking the user input pridicding output acordingly
if medical_cause == 'Y':#checking the condition 1
 print ("You are allowed")
else:
 if atten>75: #checking the condition 2
  print("Allowed")
 else:
  print("Not allowed")