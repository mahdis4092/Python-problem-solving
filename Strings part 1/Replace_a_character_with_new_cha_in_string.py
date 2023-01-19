#option 1
s="Hello"
new_s=""
curr_char="l"
new_char="e"
for char in s:
    if char==curr_char:
        new_s+=new_char
    else:
        new_s+=char
print(new_s)
#option -2 using built-in method
R='Pythonpower'
curr_char1="P"
new_char1="X"
print(R.replace(curr_char1,new_char1))