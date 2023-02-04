n=[2,4,5,6]
def Findsum(n):
    if len(n)==0:
        return 0
    else:
        return n[0]+Findsum(n[1::])
print(Findsum(n))
#option-2 sum of digit
def sumofdigit(s):
    if s==0:
        return 0
    else:
        return s%10 +sumofdigit(s//10)
print(sumofdigit(123))