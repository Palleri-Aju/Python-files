'''                     
                        Experiment -2
Name :
Class: SE-IT
Div  :
Roll number:
--------------------------------------
AIM: Write a menu driven python program to check 
if number and string is palindrome and find the factorial 
of the input number.
'''
def palindrome(n):
    a=n
    m=n
    rev=0
    while(m!=0):
        p=m%10
        m=m//10
        rev=rev*10+p
    if a==rev:
        print(n,'is a Number Palindrome')
    else:
        print(n,'is not a Number  Palindrome')

def str_pal(s):
    a=s[::-1]
    if a==s:
        print(s,"is a String Palindrome")
    else:
        print(s,"is not a String Palindrome")
        
def fact(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print("Factorial of",n,"=",fact)    

choice=0
while(choice!=4):
    print("\nEnter Your Choice:\n1.Check if number is Palindrome\n2.Check if String is Palindrome\n3.Find Factorial\n4.Exit")
    choice=int(input('Enter choice:'))
    if choice==1:
        n=int(input("Enter a number to check if it is palindrome:"))
        palindrome(n)
    elif choice==2:
        str=input("Enter a String to check if it is palindrome:")
        str_pal(str)
    elif choice==3:
        n=int(input("Enter a number :"))
        fact(n)
    elif choice==4:
        print("Thank you!!")
    else:
        print("Invalid input!!!")

'''
Output:
Enter Your Choice:
1.Check if number is Palindrome
2.Check if String is Palindrome
3.Find Factorial
4.Exit
Enter choice:1
Enter a number to check if it is palindrome:12321
12321 is a Number Palindrome

Enter Your Choice:
1.Check if number is Palindrome
2.Check if String is Palindrome
3.Find Factorial
4.Exit
Enter choice:2
Enter a String to check if it is palindrome:nitin
nitin is a String Palindrome

Enter Your Choice:
1.Check if number is Palindrome
2.Check if String is Palindrome
3.Find Factorial
4.Exit
Enter choice:3
Enter a number :4
Factorial of 4 = 24

Enter Your Choice:
1.Check if number is Palindrome
2.Check if String is Palindrome
3.Find Factorial
4.Exit
Enter choice:6
Invalid input!!!

Enter Your Choice:
1.Check if number is Palindrome
2.Check if String is Palindrome
3.Find Factorial
4.Exit
Enter choice:4
Thank you!!
'''