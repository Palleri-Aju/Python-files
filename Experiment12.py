'''                    
                        Experiment -12
Name :
Class: SE-IT
Div  :
Roll number:
--------------------------------------

Topic- File handling in Python
AIM- Write a program to write multiple statements in a text file.
	Open the same text file in read mode and count the number of words in the file
'''

#Writing into a file using write() method
f = open("E:\\python files\demofile.txt", "w")
ch=1
while ch==1:
	stm=input("Enter Statement to be added to the file :\n")
	f.write(stm+"\n")
	ch=int(input("\nEnter 1 to add more statement to the file :"))
	print("----------------------------------------------------")
f.close()

#Reading from the file and count the number of words in the file
f = open("E:\\python files\demofile.txt", "r")
#print(f.read())
#print(f.readline())
print("----------------------")
print("Text in the file:\n")
print(f.read())
print("----------------------")

f.seek(0,0)#moves the file pointer to the begining of the file

num_words=0
for x in f:
	words = x.split()
	num_words += len(words)

print("Number of words:")
print(num_words)
f.close()

'''
Output:

Enter Statement to be added to the file :
Hello, welcome to programming

Enter 1 to add more statement to the file :1
----------------------------------------------------
Enter Statement to be added to the file :
Python is easy and fun to learn

Enter 1 to add more statement to the file :0
----------------------------------------------------
----------------------
Text in the file:

Hello, welcome to programming
Python is easy and fun to learn
----------------------
Number of words:
11
