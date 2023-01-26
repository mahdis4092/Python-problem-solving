#mysolution
mylist=[1,1,2,4,6,7,6,'a','b','a']
if len(mylist)!=0:
    remove_duplicate = list(set(mylist))
    print(remove_duplicate)

else:
    print(mylist)
#To maintain same order use dictionaries
P=[1,1,2,4,6,7,6]
re_duplicate =list(dict.fromkeys(P))
print(re_duplicate)