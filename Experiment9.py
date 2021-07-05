'''                     
                        Experiment -9
Name :
Class: SE-IT
Div  :
Roll number:
--------------------------------------

Topic-Modules in Python
AIM-Creating User-defined modules/packages and import them in a program
    Program calculates BMI of a person and catgorize it as Underweight, Normal, Overweight, Obese
'''
# module.py

category=["Underweight","Normal","Overweight","Obese"]

def greeting(name):
  print("Hello, " + name)

def calculateBMI(wt,ht):
	bmi=wt/pow(ht,2)
	return bmi

#Save code in different files to execute
# TestModule.py

import module as md

name=input("Enter your name :")
wt=int(input("Enter your wight in kg :"))
ht=float(input("Enter your height in meter :"))
print("-------------------------------------")

md.greeting(name)
bmi=md.calculateBMI(wt,ht)
print("Your BMI is :",bmi)

if bmi<18.5:
	print("You are ",md.category[0])
elif bmi>=18.5 and bmi<25:
	print("You are ",md.category[1])
elif bmi>=25 and bmi<30:
	print("You are ",md.category[2])
else:
	print("You are ",md.category[3])

'''
Output:

Enter your name :Jatin
Enter your wight in kg :75
Enter your height in meter :1.8
-------------------------------------
Hello, Jatin
Your BMI is : 23.148148148148145
You are  Normal

*************************************

Enter your name :Midhun
Enter your wight in kg :95
Enter your height in meter :1.6
-------------------------------------
Hello, Midhun
Your BMI is : 37.10937499999999
You are  Obese