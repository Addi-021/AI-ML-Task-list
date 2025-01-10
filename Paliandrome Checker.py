#Paliandrome Checker for a String
string = input("Enter any Word : ")
if (string==string[::-1]):     
   print("The Word is Paliandrome")
else:
    print("The word is Not a Palinadrome")