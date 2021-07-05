'''                    
                        Experiment -13
Name :
Class: SE-IT
Div  :
Roll number:
--------------------------------------

Topic- Numpy array in Python
AIM- Write a program to add and mutiply 2-D array using numpy array
'''

import numpy as np

row=int(input("Enter number of rows:"))
col=int(input("Enter number of cols:"))
shape_mat=(row,col)
arr1=np.empty(shape_mat,dtype=int)
arr2=np.empty(shape_mat,dtype=int)
#print(arr1.shape)

print("Enter values for first Matrix :")
for x in range(row):
    for y in range(col):
        val=int(input("Enter a number :"))
        arr1[x,y]=val

print("Enter values for Second Matrix :")
for x in range(row):
    for y in range(col):
        val=int(input("Enter a number :"))
        arr2[x,y]=val

print("----------------------------------")
print("Matrix 1:")
print(arr1)
print("Matrix 2:")
print(arr2)
print("----------------------------------")
arr_add=arr1+arr2
print("Addition of two matrix is :")
print(arr_add)
print("----------------------------------")
print("Multiplication of two matrix is : ")
arr_mul=np.matmul(arr1,arr2)
print(arr_mul)

'''
Output:

Enter number of rows:2
Enter number of cols:2
Enter values for first Matrix :
Enter a number :1
Enter a number :2
Enter a number :3
Enter a number :4
Enter values for Second Matrix :
Enter a number :5
Enter a number :6
Enter a number :7
Enter a number :8
----------------------------------
Matrix 1:
[[1 2]
 [3 4]]
Matrix 2:
[[5 6]
 [7 8]]
----------------------------------
Addition of two matrix is :
[[ 6  8]
 [10 12]]
----------------------------------
Multiplication of two matrix is :
[[19 22]
 [43 50]]

'''