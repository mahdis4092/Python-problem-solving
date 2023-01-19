#my solution
p="Hello"
i=1
if len(p)==0:
    print("string are empty")
elif i>len(p)-1:
    print("index out of string : ",p)
else :
    new_p = ""
    for k in range(len(p)):
        if k!=i:
            new_p += p[k]
    print(new_p)

#or
'''
if(len(p)==0) or (i>=len(p)):
    print(p)
'''