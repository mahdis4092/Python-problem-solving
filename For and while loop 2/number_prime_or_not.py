num=int(input("Enter the given numbers: "))
is_prime=True
if num==1 or num==0:
    is_prime=False

else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

if is_prime: #check if is_prime is true of false
    print("Prime")
else:
    print("Not Prime")
