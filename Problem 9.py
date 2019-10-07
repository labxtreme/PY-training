"""
Q9.Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT
"""


_=[]
str=input("Enter lines: \n")
_.append(str)
while str:
    str=input()
    if str:
        _.append(str)    
for line in _:
    print(line.upper())
	

