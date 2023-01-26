#Lists are python form of array
x=[1,2,3]
print(x)
print(len(x))
mylist=['abc',4,25.6,[6,7,9]]
print(mylist)
k=['a','b','c','d','e']
print(k[1])
print(k[-1])
print(k[0:4])
#list are mutable

k[0]='Mahdi'
print(k)#outpt-['Mahdi', 'b', 'c', 'd', 'e']
k.append('new Item')# add item in last
print(k)
k.extend(['x','y','z'])
print(k)#output ['Mahdi', 'b', 'c', 'd', 'e', 'new Item', 'x', 'y', 'z']

#remove item
G=['a','k','f','b','c']
remove=G.pop()
print(G)#['a', 'k', 'f', 'b']
print(remove)#c
print(G.pop(2))
print(G) #['a', 'k', 'b']
#reverse
U=['1','2','3','4','5']
U.reverse()
print(U)#['5', '4', '3', '2', '1']
#sort
L=[6,8,3,90,7,1]
L.sort()
print(L)#[1, 3, 6, 7, 8, 90]

#nested list
N_list=[1,2,['a','b','c']]
print(N_list[2][1]) #output b

#List comprehension
matrix=[[1,2,3],[4,5,6],[7,8,9]]
first_col=[row[0] for row in matrix]
print(first_col) # [1, 4, 7]


