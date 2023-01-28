#Option 1
ListA=[1,2,3,4]
ListB=[3,4]
Difference=[]
for elem in ListA:
    if  elem not in ListB:
        Difference.append(elem)
print(Difference)



