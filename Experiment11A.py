'''                    
                        Experiment -11-A
Name :
Class: SE-IT
Div  :
Roll number:
--------------------------------------

Topic- Multithreading in Python
AIM- Write a multithreaded program to print hello and Hi alternately.
'''
from time import sleep
from threading import *

class Hello(Thread):
    def run(self):
        for i in range(4):
            print("Hello")
            sleep(0.49)


class Hi(Thread):
    def run(self):
        for i in range(4):
            print("Hi")
            sleep(0.5)


t1 = Hello()
t2 = Hi()

t1.start()
sleep(0.2)
t2.start()

t1.join()
t2.join()

print("Bye")

'''
Output:

Hello
Hi
Hello
Hi
Hello
Hi
Hello
Hi
Bye

'''