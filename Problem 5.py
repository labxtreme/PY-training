"""
Q5. Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
"""


class C1:
     def __init__(self):
             self.str=""
     def getstring(self):
             self.str=input("Enter a string\n")
     def printstring(self):
             print(self.str.upper())
obj=C1()
obj.getstring()
obj.printstring()



