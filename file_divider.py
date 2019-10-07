f=open("MySolution.py","r")
contents=f.read()
list_of_Questions=[]
for val in range(1,18):
    substr1="\"\"\"\nQ"+str(val)
    ind1=contents.find(substr1)
    substr2="\"\"\"\nQ"+str(val+1)
    ind2=contents.find(substr2)
    list_of_Questions.append([ind1,ind2])

for val in range(17):
    fname="Problem "+str(val+1)+".py"
    f = open(fname, "w")
    f.write(contents[list_of_Questions[val][0]:list_of_Questions[val][1]])
    f.close()
