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


