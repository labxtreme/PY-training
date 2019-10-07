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


