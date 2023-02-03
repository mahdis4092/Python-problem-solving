#option-1
s="Hello"
for char in s[::-1]:
    print(char,end="")
#option-2
A="Python"
for i in reversed(A):
    print(i,end="")
#option-3
K="World"
for j in range(len(K)-1,-1,-1):
    print(K[j],end="")
