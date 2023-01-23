#my_solution
'''import string
s="Hello World"
space=" "
new_char=""
new_s=s.lower()
print(new_s)
new_s=new_s.split(" ")
print(sorted(new_s))
if new_s!=space:
     for char in new_s:
          new_char+=char
          sort_s=sorted(new_char)
print(sort_s)
'''
#Given Solution[accurate]

s='Hello World'
new_s=""
word_list=s.split()
#print(word_list)
for word in word_list:
    lower_word=word.lower()
    #print(lower_word)
    sorted_word="".join(sorted(lower_word))
    #print(sorted_word)
    new_s+=sorted_word+" "
new_s.rstrip()
print(new_s)

