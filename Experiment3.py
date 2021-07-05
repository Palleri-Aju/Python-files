'''                     
                        Experiment -3
Name :
Class: SE-IT
Div  :
Roll number:
--------------------------------------
Aim:Write a menu driven program to demonstrate use of list in python
1.Show Even and Odd Lists
2.Merge Even and odd lists and Sort in Ascending order
3.Find Max and Min number
4.Delete a number in the list
5.Change list elements
'''
list1=[]
even=[]
odd=[]
   
def create_evenodd():
    global list1
    for n in list1:
        if n%2==0:
            even.append(n)
        else:
            odd.append(n)
    
def merge():
    global list1
    list1= even + odd
    print("Merged list:",list1)
    
def list_sort():
    global list1
    print('Unsorted list:',list1)
    list1.sort()
    print("Sorted list:",list1)
    
def maxmin():
    global list1
    print('Maximum:',max(list1))
    print('Minimum:',min(list1))
    
def deleteElement():
    global list1
    print("List elements: ", list1)
    n=int(input("Enter element to be deleted :"))
    if n in list1:
        list1.remove(n)
        print("After deleting list :",list1)
    else:
        print("Entered number not in the list")

def list_inp():
    global list1
    list1.clear ()
    num=int(input("Enter number of elements in the list :"))
    for i in range(num):
        list1.append(int(input("Enter number :")))
    print("List elements :",list1)
    
count=0
choice=0
while(choice!=6):
    if count==0:
        list_inp()  
    count+=1
    print("-------------------------------------------------------")
    print('1.Show Even and Odd Lists')
    print('2.Merge Even and odd lists and Sort in Ascending order')
    print('3.Find Max and Min number')
    print('4.Delete a number in the list')
    print('5.Change list elements')
    print('6.Exit')
    print("-------------------------------------------------------\n")
    choice=int(input('Enter Choice:'))
    if choice==1:
        create_evenodd()
        print("Even list:\n",even)
        print("Odd list:\n",odd)
    elif choice==2:
        if len(list1)==0:
            create_evenodd()
        merge()
        list_sort()    
    elif choice==3:
        maxmin()
    elif choice==4:
        deleteElement()
    elif choice==5:
        list_inp()
    elif choice==6:
        print("Thank You!!!")
        continue
    else:
        print("Invalid input")
'''
Output:

Enter number of elements in the list :5
Enter number :1
Enter number :2
Enter number :3
Enter number :4
Enter number :5
List elements : [1, 2, 3, 4, 5]
-------------------------------------------------------
1.Show Even and Odd Lists
2.Merge Even and odd lists and Sort in Ascending order
3.Find Max and Min number
4.Delete a number in the list
5.Change list elements
6.Exit
-------------------------------------------------------

Enter Choice:1
Even list:
 [2, 4]
Odd list:
 [1, 3, 5]
-------------------------------------------------------
1.Show Even and Odd Lists
2.Merge Even and odd lists and Sort in Ascending order
3.Find Max and Min number
4.Delete a number in the list
5.Change list elements
6.Exit
-------------------------------------------------------

Enter Choice:2
Merged list: [2, 4, 1, 3, 5]
Unsorted list: [2, 4, 1, 3, 5]
Sorted list: [1, 2, 3, 4, 5]
-------------------------------------------------------
1.Show Even and Odd Lists
2.Merge Even and odd lists and Sort in Ascending order
3.Find Max and Min number
4.Delete a number in the list
5.Change list elements
6.Exit
-------------------------------------------------------

Enter Choice:3
Maximum: 5
Minimum: 1
-------------------------------------------------------
1.Show Even and Odd Lists
2.Merge Even and odd lists and Sort in Ascending order
3.Find Max and Min number
4.Delete a number in the list
5.Change list elements
6.Exit
-------------------------------------------------------

Enter Choice:4
List elements:  [1, 2, 3, 4, 5]
Enter element to be deleted :4
After deleting list : [1, 2, 3, 5]
-------------------------------------------------------
1.Show Even and Odd Lists
2.Merge Even and odd lists and Sort in Ascending order
3.Find Max and Min number
4.Delete a number in the list
5.Change list elements
6.Exit
-------------------------------------------------------

Enter Choice:5
Enter number of elements in the list :6
Enter number :1
Enter number :2
Enter number :3
Enter number :4
Enter number :5
Enter number :6
List elements : [1, 2, 3, 4, 5, 6]
-------------------------------------------------------
1.Show Even and Odd Lists
2.Merge Even and odd lists and Sort in Ascending order
3.Find Max and Min number
4.Delete a number in the list
5.Change list elements
6.Exit
-------------------------------------------------------

Enter Choice:6
Thank You!!!
'''