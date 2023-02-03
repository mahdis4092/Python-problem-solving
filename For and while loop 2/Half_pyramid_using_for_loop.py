num=int(input("Enter the number of row: "))
k=(num*2)-2
for i in range(0,num):
    #for space
    for j in range(0,k):
        print(" ",end="")
    k=k-2
    for j in range(0,i+1):
        print("*",end=" ")
    print(" ")
