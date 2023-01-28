import itertools
myList=[1,2,3]
permuations=list(itertools.permutations(myList))
#print(permuations)
for p in permuations: #new line every elements
    print(p)