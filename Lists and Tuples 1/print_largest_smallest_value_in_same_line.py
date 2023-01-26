#my-solution
myList=[3,7,5,1,4]
if myList!=[]:
    max_num=max(myList)
    min_num=min(myList)
    print(max_num,end=" ")
    print(min_num)
else:
    print(myList)
#given-solution
P=[3,7,5,1,4]
if P:
    print(max(P),min(P))
else:
    print(None)
