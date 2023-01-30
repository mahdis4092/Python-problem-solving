first_value=int(input("Please enter the first value: "))
second_value=int(input("Please enter the first value: "))
print("Great! Now enter the operation.")
print("These are the available options:")
print("1 - Addition\n2 - Subtraction\n3 - Multiplication\n4 - Division\n5 - Integer Division\n6 - Modulo")
option=int(input("Enter the corresponding integer: "))
if option==1:
    sum=first_value+second_value
    print(f"The result of {first_value}+{second_value} is {sum} ")
elif option==2:
    sub = first_value - second_value
    print(f"The result of {first_value}-{second_value} is {sub} ")
elif option==3:
    mul=first_value*second_value
    print(f"The result of {first_value}*{second_value} is {mul} ")
elif option==4:
    div=first_value/second_value
    print(f"The result of {first_value}/{second_value} is {div} ")
elif option==5:
    indiv=first_value//second_value
    print(f"The result of {first_value}//{second_value} is {indiv} ")
else:
    mod=first_value%second_value
    print(f"The result of {first_value}%{second_value} is {mod} ")



