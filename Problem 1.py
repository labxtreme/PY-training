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





