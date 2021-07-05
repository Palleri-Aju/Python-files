'''						
						Experiment -1
Name :
Class: SE-IT
Div	 :
Roll number:
--------------------------------------
AIM: Write a python program to  check if the entered numbers are
positive or negative or zero also swap two numbers and display results
'''

a=int(input("Enter first no:"))
b=int(input("Enter second no:"))
print()

print("----------------------------------------")
print("Checking if numbers are -ve, +ve or zero")
if a>0:
    print("First number a = ",a," is positive")
elif a<0:
    print("First number a = ",a," is negative")
else:
    print("First number is zero")

if b>0:
    print("Second number b = ",b," is positive")
elif b<0:
    print("Second number b = ",b," is negative")
else:
    print("Second number zero")
print("----------------------------------------")
print("Swapping two numbers")
print("Before swapping a=",a," b=",b)
a,b=b,a
print("After swapping a=",a," b=",b)

'''
Output:
Enter first no:12
Enter second no:-23

----------------------------------------
Checking if numbers are -ve, +ve or zero
First number a =  12  is positive
Second number b =  -23  is negative
----------------------------------------
Swapping two numbers
Before swapping a= 12  b= -23
After swapping a= -23  b= 12
'''


