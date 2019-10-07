"""
Q20.
A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT
with a given steps. The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
¡­
The numbers after the direction are steps. Please write a program to compute the distance from current position after a
sequence of movement and original point. If the distance is a float, then just print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2
"""
import math
P,B=0,0
li=[]
instruction=input("Enter lines: \n")
li.append(instruction.split())
while instruction:
    instruction=input()
    if instruction:
        li.append(instruction.split())
for val in li:
    if(val[0]=="UP"):
        P+=int(val[1])
    if(val[0]=="DOWN"):
        P-=int(val[1])
    if(val[0]=="LEFT"):
        B+=int(val[1])
    if(val[0]=="RIGHT"):
        B-=int(val[1])
H=round(math.sqrt(P*P+B*B))
print(H)
