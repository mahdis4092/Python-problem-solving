arr=[]
kth_element=3
n=int(input("Enter the number of array size"))
for i in range(n):
   value=int(input())
   arr.append(value)
print(arr)
#print(arr[2])
new_arr=sorted(arr)
print(new_arr)
print(new_arr[len(new_arr) - kth_element])

