'''                     
                        Experiment -4	
Name :
Class: SE-IT
Div  :
Roll number:
--------------------------------------
Topic : Python Tuple
Aim: Write a menu driven program to demonstrate the use of nested tuples in python
	1.Display All student records
	2.Search a student and display its records
	3.Delete a student from the tuple
	4.Sort the tuple
	5.Exit
'''
import os
student=[]
def addStudentRecords():
	global student
	n=int(input("Enter number of students :"))
	for i in range(n):
		print("--------------------------------------")
		r_no=int(input("Enter student roll number :"))
		name=input("Enter student name :")
		sub1=int(input("Enter marks in subject 1 :"))
		sub2=int(input("Enter marks in subject 2 :"))
		sub3=int(input("Enter marks in subject 3 :"))
		templist=(r_no,name,sub1,sub2,sub3)
		student.append(templist)
		#print("--------------------------------------")
	_ = os.system('cls')#this statement will work on windows only
	print('Student Records stored in nested tuples')
	global studTuple
	studTuple=tuple(student)
	#print(student)
	print(studTuple)
'''
def studList():
    x=int(input("Enter the number of students you want to enter:"))
    global inp
    for i in range(x):
        student.append(eval(input("Enter student details \nIn the form Rollno,'Name',Marks1,Marks2,Marks3:\n")))
        print(student)
'''
def searchStudent():
	global studTuple
	sname=input("Enter student name to be searched :")
	found=False
	for x in student:
		if sname in x:
			found=True
			print("Student roll no:",x[0])
			print("Student marks:",x[2:5])
	if found==False:
		print("Student record not found in tuple")

def deleteStudent():
	global studTuple
	sname=input("Enter student name to be deleted :")
	found= False
	for x in student:
		if sname in x:
			found=True
			student.remove(x)
			print("Record of ",sname," student deleted successfully")
			studTuple=tuple(student)
	if found==False:
		print(sname," student not found in records ")

    
def sortTuple():
	global studTuple
	global student
	print("Tuple sorted wrt Roll number:",sorted(student))
	print("Tuple sorted wrt Name:",sorted(student,key=lambda x:x[1]))
	#print(student)

count=0
choice=0
while(choice!=5):
	if count==0:
		addStudentRecords()
	count+=1
	print("-------------------------------------------")
	print("1.Display All student records")
	print("2.Search a student and display its records")
	print("3.Delete a student from the tuple")
	print("4.Sort the tuple")
	print("5.Exit")
	print("-------------------------------------------")
	choice=int(input("\nEnter Your Choice: "))
	if choice==1:
		print(studTuple)
	elif choice==2:
		searchStudent()
	elif choice==3:
		deleteStudent()
	elif choice==4:
		sortTuple()
	elif choice==5:
		print("Thank You!!!")
		exit(0)
	else:
		print("Invalid input")

'''
Output:
Enter number of students :4
--------------------------------------
Enter student roll number :110
Enter student name :Manish
Enter marks in subject 1 :45
Enter marks in subject 2 :56
Enter marks in subject 3 :67
--------------------------------------
Enter student roll number :105
Enter student name :Dinesh
Enter marks in subject 1 :55
Enter marks in subject 2 :66
Enter marks in subject 3 :77
--------------------------------------
Enter student roll number :108
Enter student name :Mayur
Enter marks in subject 1 :54
Enter marks in subject 2 :65
Enter marks in subject 3 :76
--------------------------------------
Enter student roll number :101
Enter student name :Rahul
Enter marks in subject 1 :87
Enter marks in subject 2 :78
Enter marks in subject 3 :45

Student Records stored in nested tuples
((110, 'Manish', 45, 56, 67), (105, 'Dinesh', 55, 66, 77), (108, 'Mayur', 54, 65, 76), (101, 'Rahul', 87, 78, 45))
-------------------------------------------
1.Display All student records
2.Search a student and display its records
3.Delete a student from the tuple
4.Sort the tuple
5.Exit
-------------------------------------------

Enter Your Choice: 1
((110, 'Manish', 45, 56, 67), (105, 'Dinesh', 55, 66, 77), (108, 'Mayur', 54, 65, 76), (101, 'Rahul', 87, 78, 45))
-------------------------------------------
1.Display All student records
2.Search a student and display its records
3.Delete a student from the tuple
4.Sort the tuple
5.Exit
-------------------------------------------

Enter Your Choice: 2
Enter student name to be searched :Rajesh
Student record not found in tuple
-------------------------------------------
1.Display All student records
2.Search a student and display its records
3.Delete a student from the tuple
4.Sort the tuple
5.Exit
-------------------------------------------

Enter Your Choice: 2
Enter student name to be searched :Rahul
Student roll no: 101
Student marks: (87, 78, 45)
-------------------------------------------
1.Display All student records
2.Search a student and display its records
3.Delete a student from the tuple
4.Sort the tuple
5.Exit
-------------------------------------------

Enter Your Choice: 3
Enter student name to be deleted :Rahul
Record of  Rahul  student deleted successfully
-------------------------------------------
1.Display All student records
2.Search a student and display its records
3.Delete a student from the tuple
4.Sort the tuple
5.Exit
-------------------------------------------

Enter Your Choice: 1
((110, 'Manish', 45, 56, 67), (105, 'Dinesh', 55, 66, 77), (108, 'Mayur', 54, 65, 76))
-------------------------------------------
1.Display All student records
2.Search a student and display its records
3.Delete a student from the tuple
4.Sort the tuple
5.Exit
-------------------------------------------

Enter Your Choice: 4
Tuple sorted wrt Roll number: [(105, 'Dinesh', 55, 66, 77), (108, 'Mayur', 54, 65, 76), (110, 'Manish', 45, 56, 67)]
Tuple sorted wrt Name: [(105, 'Dinesh', 55, 66, 77), (110, 'Manish', 45, 56, 67), (108, 'Mayur', 54, 65, 76)]
-------------------------------------------
1.Display All student records
2.Search a student and display its records
3.Delete a student from the tuple
4.Sort the tuple
5.Exit
-------------------------------------------

Enter Your Choice: 5
Thank You!!!