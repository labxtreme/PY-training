"""
Q1. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
"""



begin = 2000
end = 3201
list=[]
for _ in range(begin,end):
     if _%7==0:
             if _%5!=0:
                     list.append(str(_))
print(','.join(list))





"""
Q2. Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320
"""




def fact(num):
     if num == 1:
             return 1
     else :
             return num*fact(num-1)
num=int(input("Enter a number:"))
print(fact(num))




"""
Q3. With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
"""



di=dict()
num=int(input("Enter a number:"))
for _ in range(1,num+1):
     di[_]=_*_
print(di)




"""
Q4. Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
"""



values=list(map(int,(input("Enter the values: ").split(","))))
print(values)
print(tuple(values))



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



"""
Q6. Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24
"""

import math
C=50
H=30
values=list(map(int,(input("Enter the values: ").split(","))))
def F1(num):
	res=math.sqrt((2*C*num)/H)
	return str(round(res))
li=list(map(F1,values))
print(','.join(li))


"""
Q7.Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,��Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
"""


X,Y=map(int,input("Enter X and Y \n").split(","))
liMajor=[]
for i in range(X):
	liMinor=[]
	for j in range(Y):
		liMinor.append(i*j)
	liMajor.append(liMinor)
print(liMajor)


"""
Q8.Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world
"""

_=input("Enter the string: \n").split(",")
_.sort()
print(','.join(_))


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


"""
Q10.Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world
"""


_=input("Enter the Line : \n").split()
_=list(set(_))
_.sort()
print(' '.join(_))


"""
Q11.Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.
"""


val=input("Enter the values:\n").split(",")
sol=[]
print(val)
for i in range(len(val)):
	if int(val[i],2)%5==0:
		sol.append(val[i])
print(",".join(sol))


"""
Q12.Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
"""

sol=[]
for _ in range(1000,3001):
    temp=_
    flag=1
    while(temp):
        num=temp%10
        temp=temp//10
        if num%2==0 and flag:
            pass
        else:
            flag=0
            break
    if flag:
        sol.append(str(_))
print(','.join(sol))


"""
Q13.Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
"""

string = input("Enter the string : \n")
letter=0
digits=0
for char in string:
    if char.isalpha():
        letter+=1
    if char.isnumeric():
        digits+=1
print("LETTERS {0} \nDIGITS {1}".format(letter,digits))


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


"""
Q15.Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106
"""

a=input("Enter the Number: \n")
sum=0
v=a
for val in range(4):
    sum=int(v)+sum
    v=v+a
print(sum)

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


"""
Q17.A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1
"""
def validator(password):
   flag=list("0000")
   if len(password)<=12 and len(password)>6:
       print(len(password))
       for val in password:
            if val.islower():
                flag[0]='1'
            if val.isupper():
                flag[1]='1'
            if val=='#' or val=='$' or val=='@':
                flag[2]='1'
            if val.isnumeric():
                flag[3]='1'
   print("".join(flag))
   if "".join(flag)=="1111":
       return password
   else:
        pass

string=input("Enter the Passwords: \n").split(',')
valid=list(map(validator,string))
valid=[password for password in valid if password]
print(",".join(valid))
