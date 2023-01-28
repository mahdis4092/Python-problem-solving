#my solution
myList=[1,2,9,10,7,8]
new_mylist=sorted(myList)
print(new_mylist[len(new_mylist)-2])
#Given Solution
P=[1,6,7,5]
if len(P)>1:
    sorted_lists=sorted(P)
    print(sorted_lists[-2])
else:
    print(None)