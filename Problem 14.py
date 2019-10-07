"""
Q14.Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
"""

string = input("Enter the string : \n")
Upper=0
Lower=0
for char in string:
    if char.isupper():
        Upper+=1
    if char.islower():
        Lower+=1
print("UPPER CASE {0} \nLOWER CASE {1}".format(Upper,Lower))

		
