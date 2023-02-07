n=int(input("Enter the number"))
first=n
last=0
for i in reversed(range(first,last,-1)):
    increment = (i * 2)
    for j in range(1,increment):
        print("*",end=" ")

    print()



'''
n=int(input())
for i in reversed(range(n,0,-1)):
    for j in range(i):
        print("*",end=" ")
    print()
print(reversed)
'''