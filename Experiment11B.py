'''                    
                        Experiment -11-B
Name :
Class: SE-IT
Div  :
Roll number:
--------------------------------------

Topic- Multithreading in Python
AIM- Write a multithreaded program to print square and cube of numbers in a list.
	Set target methods to execute on call of thread start method
'''
import time
import threading

def calc_square(numbers):
    #print("calculate square numbers")
    for n in numbers:
        print('square of ',n, ' :',n*n)
        time.sleep(1)

def calc_cube(numbers):
    #print("calculate cube of numbers")
    for n in numbers:
        print('cube of ',n,' :',n*n*n)
        time.sleep(1)

arr = [2,3,8,9]

t = time.time()

t1= threading.Thread(target=calc_square, args=(arr,))
t2= threading.Thread(target=calc_cube, args=(arr,))

t1.start()
time.sleep(0.2)
t2.start()

t1.join()
t2.join()

print("Executed in : ",time.time()-t)
print("End of Main thread!!!")