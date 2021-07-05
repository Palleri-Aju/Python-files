'''                     
                        Experiment -8
Name :
Class: SE-IT
Div  :
Roll number:
--------------------------------------

Topic-Inheritance in Python
AIM-1. Create a class Person with properties firstname, lastname, age, displayDetails().
    2. Create class Employee that derives from class Person. 
    3. Class Employee has staffnumber and overrides displayDetails(),displayEmployeeSalaray()
    4. Create an object of child class and access methods
'''
class Person:
    def __init__(self, first, last, age):
        self.firstname = first
        self.lastname = last
        self.age = age
 
    def displayDetails(self):
        return self.firstname + " " + self.lastname + ", " + str(self.age)
 
class Employee(Person):
 
    def __init__(self, first, last, age, staffnum):
        Person.__init__(self,first, last, age)
        self.staffnumber = staffnum
 
    def displayDetails(self):
         return self.firstname + " " + self.lastname + ", " + str(self.age)+ ", " + str(self.staffnumber)
 
    def displayEmployeeSalaray(self,basic,hra=None):
        if hra is not None:
           self.salary=basic+hra 
        else:
            self.salary=basic
        print ("Salary :",self.salary)
            
x = Person("Jim", "Halpert", 36)
y = Employee("Pam", "Halpert", 28, "100")
 
print(x.displayDetails())
print(y.displayDetails())
 
y.displayEmployeeSalaray(10000)
y.displayEmployeeSalaray(15000,5000)
#print(y.salary)