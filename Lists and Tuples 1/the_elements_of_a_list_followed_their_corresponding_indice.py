#Option-1[regular method]
myList=['a','b','c',8,9]
if len(myList)!=0:
    for i in range(len(myList)):
        print(myList[i],i)
else:
    print("Empty List")


#Option-2
P=[2,5,7,8,9]
if not P:
    print("Empty List")
else:
    for j,elem in enumerate(P):
        print(elem, j)

