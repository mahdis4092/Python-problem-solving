#my solution-not complete
'''myList=[1,2,3,4]
remove_element=2
new_list=[]
remove_list=[]
if len(myList)!=0:
    for i in range(len(myList)):
        if myList[i]!=remove_element:
            new_list+= myList

        else:
            remove_list+=myList

    print(new_list)

else:
    print("Empty List")
'''
#Given Solution
myList=['a','b',2,'a']
elem_to_remove=2
if len(myList)==0:
    print('Empty List')
elif myList.count(elem_to_remove)==0:
    print("Element not Found")
else:
    for i in range(myList.count(elem_to_remove)):
        myList.remove(elem_to_remove)
    print(myList)

