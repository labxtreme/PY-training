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

