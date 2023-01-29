#option-1
a=int(input("Give First Number: "))
b=int(input("Give Second Number: "))
c=int(input("Give Third Number: "))
if a>=b and a>=c:
    print(f"{a} is a maximum".format(a))
elif b>=a and b>=c:
    print(f"{b} is a maximum".format(b))
else:
    print(f"{c} is a maximum".format(c))

#option-2
print(max(2,10,5))