# Basic Calculator taking user input
print("WELCOME TO CALCULATOR")
num1 = input("Enter first value : ") #Input from the user 
print   ("Select Operation")
print   ("1. Addition ")
print   ("2. Subtraction")
print   ("3. Multiplication")
print   ("4. Division")
operation = input("Enter the number corresponding to the operation (1/2/3/4) : ")
num2 = input("Enter Second value : ") #Input from the user 

if      operation == '1':
    print ("The Addition of two number is :",               int(num1)   +   int(num2 ))
elif    operation == '2' :
    print ("The Subtration of two number is :" ,            int(num1)   -   int(num2 )) 
elif    operation == '3' :
    print ("The Multiplication of first two number is : ",  int(num1)   *   int(num2 ))
elif     operation == '4':
    if num2 !=0:
        print ("The Division of two number is :",            int(num1)   /   int(num2 ))