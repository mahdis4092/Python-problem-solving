height=int(input("Enter the number of rows"))
if height%2==0:
    print("Enter the odd input ")
else:
    mid=(height+2)//2

    for i in range(mid):
        print(" " * (mid-i),"*" * ((i*2)+1))

    for i in range(mid-2,-1,-1):
        print(" " * (mid - i), "*" * ((i * 2) + 1))
