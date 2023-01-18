'''string are immutable so we cannot remove character rather
we take a new string to assign'''
s="coding"
new_s=""
for i in range(len(s)):
    if i%2!=0:
        new_s=new_s+s[i]
    print(new_s)
