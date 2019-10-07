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


