#my_solution
L=['a','b',4,5,6]
new_L=[]
factor=3
for i in L:
    new_L=i*factor
    print(new_L)

#given solution[accurate]
P=[2,4,6,'b','c']
factor=3
for i in range(len(P)):
    P[i]*=factor

print(P)