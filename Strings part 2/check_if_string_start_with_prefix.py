#Option-1
s="Hello"
prefix="He"
if s[:len(prefix)]==prefix:
    print(True)
else:
    print(False)

#Option-2 = more precise
A="coding"
prefix1="co"
print(A.startswith(prefix1))
