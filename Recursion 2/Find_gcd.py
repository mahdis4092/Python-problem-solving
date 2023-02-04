def Find_gcd(a,b):
    if b==0:
        return a
    else:
        return Find_gcd(b,a%b)
print(Find_gcd(42,56))