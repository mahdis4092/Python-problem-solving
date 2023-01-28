myList=[[1,2,3],[4,5,6],[7,8,9],10]
flat_list=[]
for elem in myList:             #check every element
    if isinstance(elem,list):    #check is any elements are list in list
        for nested_elem in elem:  # work with nested list
            flat_list.append(nested_elem)
    else:
        flat_list.append(elem)
print(flat_list)

