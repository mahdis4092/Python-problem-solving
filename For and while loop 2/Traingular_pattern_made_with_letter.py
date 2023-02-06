#option-1
n=int(input("Input: "))
count=65
for i in range(1,n+1):
    for j in range(i):
        print(chr(count),end=" ")
    count += 1
    print()

#option-2
num_rows=int(input("Input: "))
for k in range(num_rows):
    print(chr(65+k)*(k+1))