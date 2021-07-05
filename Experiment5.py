'''                     
                        Experiment -5	
Name :
Class: SE-IT
Div  :
Roll number:
--------------------------------------
Topic: Python Set
Aim: Write a menu driven program to demonstrate use of set in python
Accept two strings from the user and
1) Display Common Letters in Two Input Strings (Set Intersection)
2) Displays Letters which are in the First String but not in the Second (Set Difference)
3) Displays set of all Letters of Both the Strings (Set Union)
4) Displays Letters which are in the Two Strings but not in Both (Symmetric Difference)
'''

def str_inp():
   global str1,str2
   print("Enter first String:")
   str1=input()
   print("Enter second String:")
   str2=input()

def str_intr():
    output=list(set(str1)&set(str2))
    for x in output:
        print(x)

def str_diff():
    output=list(set(str1)-set(str2))
    for x in output:
        print(x)

def str_union():
    output=list(set(str1)|set(str2))
    for x in output:
        print(x)
        
def str_exor():
    output=list(set(str1)^set(str2))
    for x in output:
        print(x)
str1=""
str2=""
count=0

choice=0
while(choice!=5):
	if count==0:
		str1=input("Enter First String : ")
		str2=input("\nEnter Second String : ")
		count+=1
	print("----------------------------------------------------------------------")
	print("1.Display Common characters in Two Input Strings")
	print("2.Displays Letters which are in the First String but not in the Second")
	print("3.Displays set of all Letters of Both the Strings")
	print("4.Displays Letters which are in the Two Strings but not in Both")
	print("5.Exit")
	print("----------------------------------------------------------------------")
	choice=int(input("\nEnter Your Choice: "))
	if choice==1:
		str_intr()
	elif choice==2:
		str_diff()
	elif choice==3:
		str_union()
	elif choice==4:
		str_exor()
	elif choice==5:
		print("Thank You!!!")
		exit(0)
	else:
		print("Invalid input. Please input correct choice!!!")
'''
Output:

Enter First String : Jayesh

Enter Second String : Mahesh
----------------------------------------------------------------------
1.Display Common characters in Two Input Strings
2.Displays Letters which are in the First String but not in the Second
3.Displays set of all Letters of Both the Strings
4.Displays Letters which are in the Two Strings but not in Both
5.Exit
----------------------------------------------------------------------

Enter Your Choice: 1
a
h
e
s
----------------------------------------------------------------------
1.Display Common characters in Two Input Strings
2.Displays Letters which are in the First String but not in the Second
3.Displays set of all Letters of Both the Strings
4.Displays Letters which are in the Two Strings but not in Both
5.Exit
----------------------------------------------------------------------

Enter Your Choice: 2
J
y
----------------------------------------------------------------------
1.Display Common characters in Two Input Strings
2.Displays Letters which are in the First String but not in the Second
3.Displays set of all Letters of Both the Strings
4.Displays Letters which are in the Two Strings but not in Both
5.Exit
----------------------------------------------------------------------

Enter Your Choice: 3
h
s
y
a
M
e
J
----------------------------------------------------------------------
1.Display Common characters in Two Input Strings
2.Displays Letters which are in the First String but not in the Second
3.Displays set of all Letters of Both the Strings
4.Displays Letters which are in the Two Strings but not in Both
5.Exit
----------------------------------------------------------------------

Enter Your Choice: 4
M
J
y
----------------------------------------------------------------------
1.Display Common characters in Two Input Strings
2.Displays Letters which are in the First String but not in the Second
3.Displays set of all Letters of Both the Strings
4.Displays Letters which are in the Two Strings but not in Both
5.Exit
----------------------------------------------------------------------

Enter Your Choice: 5
Thank You!!!
'''