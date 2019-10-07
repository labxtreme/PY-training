"""
Q16. Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500
"""


_=[]
str=input("Enter lines: \n")
_.append(str)
while str:
    str=input()
    if str:
        _.append(str)
bal=0
for val in _:
    temp=val.split()
    if temp[0]=='D':
        bal+=int(temp[1])
    if temp[0]=='W':
        bal-=int(temp[1])
print(bal)


