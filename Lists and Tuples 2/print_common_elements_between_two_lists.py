pointA=[1,2,3,4]
pointB=[4,6]
similar=[]
for elem in pointA:
    if elem in pointB:
        similar.append(elem)
    print(similar)
