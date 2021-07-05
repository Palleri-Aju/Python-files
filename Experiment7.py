'''                     
                        Experiment -7
Name :
Class: SE-IT
Div  :
Roll number:
--------------------------------------
Topic-Classes and Objects(Array of Objects in Python)
AIM- Create a class Employee with properties name, empId, setLocation(), getLocation(), setSalary() and getSalary()
	Create N objects of Employee class and initialize members and call methods
	Create an object with name=Python, empId=20, Location=Mumbai and sal=50000
	Display Total objects of the class
'''
class Employee:
    
   employeeCount = 0
 
   
   def __init__(self, name, empId):
      self.name = name
      self.empId = empId
      Employee.employeeCount += 1
 
   def setLocation(self,empLocation):
      self.empLocation = empLocation
 
   def getLocation(self):
      return self.empLocation
 
   def setSalaray(self,empSalaray):
     self.empSalaray = empSalaray
 
   def getSalaray(self):
      return self.empSalaray
 
   @classmethod
   def displayEmployeeCount(cls):
      return cls.employeeCount
 
   def displayEmployee(self):
      print ("Employe name :",self.name," || ID : ",self.empId)
 
numberOfEmployee = int (input("Enter total number of employee : "))
print("\n")
employeeObjectList = []
n = 1
while (n<=numberOfEmployee):
   print ("Enter the detail for employee",n," :")
   inputName = input("Enter the Employee name : ")
   empId = input("Enter the Employee ID : ")
   e = Employee(inputName, empId)
   e.setLocation(input("Enter the Employee location : "))
   e.setSalaray(float(input("Enter the Employee basic salary : ")))
   employeeObjectList.append(e)
   n =  n + 1
 
print ("\nDetails of Employee ",len(employeeObjectList)," : \n")
for x in employeeObjectList:
   x.displayEmployee()
   print ("Employee location : ",x.getLocation()," || Employee salary : ",x.getSalaray())
   print("\n")

empX = Employee("Python", 20)
empX.setLocation("Mumbai")
empX.setSalaray(50000)
 
print ("Details of employee X : \n")
empX.displayEmployee()
print ("Employee location : ",empX.getLocation()," || Employee salary : ",empX.getSalaray(),"\n")
 
print ("\nTotal number of employees in the class Employee are : ",Employee.displayEmployeeCount())
