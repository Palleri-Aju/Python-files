'''                    
                        Experiment -10
Name :
Class: SE-IT
Div  :
Roll number:
--------------------------------------

Topic-Exception handling in Python(try, except, raise)
AIM- Write a program to create user defined exception in python.
    The program generates a random number between 1 to 100 and asks the user to guess the number
    The program throws a user deined exception if user guess is incorrect
    The program counts the number of guess user makes to reach the correct number
'''
import random
# define Python user-defined exceptions

class ValueTooSmallError(Exception):
    """Raised when the input value is too small"""
    pass

class ValueTooLargeError(Exception):
    """Raised when the input value is too large"""
    pass

# you need to guess this number
number = random.randint(1, 100)
count=0
# user guesses a number until he/she gets it right
while True:
    count+=1
    try:
        i_num = int(input("Enter a number: "))
        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("This value is too small, try again!")
        print()
    except ValueTooLargeError:
        print("This value is too large, try again!")
        print()

print("Congratulations! You guessed it correctly in ",count," attempts")

'''
Output:

Enter a number: 40
This value is too small, try again!

Enter a number: 60
This value is too small, try again!

Enter a number: 79
This value is too small, try again!

Enter a number: 90
This value is too large, try again!

Enter a number: 85
This value is too small, try again!

Enter a number: 88
This value is too small, try again!

Enter a number: 89
Congratulations! You guessed it correctly in  7  attempts

'''