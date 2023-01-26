myList=[7,2,3-1,4,1,8,3]
count=0
for i in range(len(myList)):
    if myList[i]>3:
        count+=1
print(count)