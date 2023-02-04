def Fibonacci(n):
    if(n<=1):
        return n
    else:
        return Fibonacci(n-2)+Fibonacci(n-1)

x=Fibonacci(6)
print(x)
