"""
Question:
Define a function with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

"""
def putNumbers(n):
    i = 0
    while i<n:
        j=i
        i=i+1
        if j%7==0:
            yield j

num=int(input("Enter a number:\n"))
a=putNumbers(num+1)
for ele in a:
        print(ele)
