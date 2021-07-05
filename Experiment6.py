'''                     
                        Experiment -6
Name :
Class: SE-IT
Div  :
Roll number:
--------------------------------------
Topic: Python Dictionary
Aim:Write a menu driven program to demonstrate use of dictionary in python
Accept values for two dictionary
    1.Concatenate elements of Dictionay
    2.Delete an element from the First dictionary
    3.Find a key and print its value
    4.Accept values into two list and Map the two list into dictionary
    5.Exit
'''
def createDict(Dict):
    n=int(input("Enter number of values:"))
    for i in range (0,n):
        key=int(input("Enter key(int):"))
        value=input("Enter value:")
        Dict.update({key:value})
    print("The dictionary is:")
    print(Dict)

def dict_concatenate():
    Dict1.update(Dict2)
    print("Dictionary after concatenation:",Dict1)
    
def dict_delete():
    m=int(input("Enter key of value to be deleted:"))
    if m in Dict1:
        print("Deleted value:",Dict1[m])
        del Dict1[m]
        print("Dictionary after deletion:",Dict1)
    else:
        print("Key not present in Dictionary")

def dict_find():
    m=int(input("Enter key to be searched:"))
    if m in Dict1:
        print("The key value is:",Dict1[m])
    else:
        print("Key not present in Dictionary")

def dict_map():
    key=[]
    values=[]
    n=int(input("Enter no of elements:"))
    for i in range (0,n):
        e1=int(input("Enter key:"))
        key.append(e1)
        e2=input("Enter value:")
        values.append(e2)
    print("Key list:",key,"\nValue list:",values)
    Dict3=dict(zip(key,values))
    print("Dictionary after mapping:",Dict3)    

Dict1={}
Dict2={}
choice=0
count=0
while(choice!=5):
    if count==0:
        print("Creating First Dictionary :")
        createDict(Dict1)
        print("---------------------------")
        print("Creating Second Dictionary :")
        createDict(Dict2)
        count+=1
    print("----------------------------------------")
    print("1.Concatenate elements of Dictionay")
    print("2.Delete an element from the dictionary")
    print("3.Find a key and print its value")
    print("4.Map two list into dictionary")
    print("5.Exit")
    choice=int(input("Enter Choice:"))
    print("----------------------------------------")
    if choice==1:
        print("Concatenating two dictionary")
        print("Dictionary 1:")
        print(Dict1)
        print("Dictionary 2:")
        print(Dict2)
        dict_concatenate()
    elif choice==2:
        print("Deleting an element by key from Dictionary 1 :")
        dict_delete()
    elif choice==3:
        print("Find an element from Dictionary 1:")
        dict_find()
    elif choice==4:
        dict_map()
    elif choice==5:
        print("Thank you")
        exit(0)
    else:
        print("Invalid Choice")

'''
Output:

Creating First Dictionary :
Enter number of values:3
Enter key(int):1
Enter value:12
Enter key(int):2
Enter value:23
Enter key(int):3
Enter value:34
The dictionary is:
{1: '12', 2: '23', 3: '34'}
---------------------------
Creating Second Dictionary :
Enter number of values:2
Enter key(int):4
Enter value:45
Enter key(int):5
Enter value:56
The dictionary is:
{4: '45', 5: '56'}
----------------------------------------
1.Concatenate elements of Dictionay
2.Delete an element from the dictionary
3.Find a key and print its value
4.Map two list into dictionary
5.Exit
Enter Choice:1
----------------------------------------
Concatenating two dictionary
Dictionary 1:
{1: '12', 2: '23', 3: '34'}
Dictionary 2:
{4: '45', 5: '56'}
Dictionary after concatenation: {1: '12', 2: '23', 3: '34', 4: '45', 5: '56'}
----------------------------------------
1.Concatenate elements of Dictionay
2.Delete an element from the dictionary
3.Find a key and print its value
4.Map two list into dictionary
5.Exit
Enter Choice:2
----------------------------------------
Deleting an element by key from Dictionary 1 :
Enter key of value to be deleted:3
Deleted value: 34
Dictionary after deletion: {1: '12', 2: '23', 4: '45', 5: '56'}
----------------------------------------
1.Concatenate elements of Dictionay
2.Delete an element from the dictionary
3.Find a key and print its value
4.Map two list into dictionary
5.Exit
Enter Choice:3
----------------------------------------
Find an element from Dictionary 1:
Enter key to be searched:4
The key value is: 45
----------------------------------------
1.Concatenate elements of Dictionay
2.Delete an element from the dictionary
3.Find a key and print its value
4.Map two list into dictionary
5.Exit
Enter Choice:4
----------------------------------------
Enter no of elements:4
Enter key:1
Enter value:2
Enter key:3
Enter value:4
Enter key:5
Enter value:6
Enter key:6
Enter value:7
Key list: [1, 3, 5, 6]
Value list: ['2', '4', '6', '7']
Dictionary after mapping: {1: '2', 3: '4', 5: '6', 6: '7'}
----------------------------------------
1.Concatenate elements of Dictionay
2.Delete an element from the dictionary
3.Find a key and print its value
4.Map two list into dictionary
5.Exit
Enter Choice:5
----------------------------------------
Thank you

'''
