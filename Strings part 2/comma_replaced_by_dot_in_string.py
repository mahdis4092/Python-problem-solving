#option-1
s="Hello, World,man"
new_s=""
new_char="."
old_char=","
for char in s:
    if char==old_char:
        new_s+=new_char
    else:
        new_s+=char
print(new_s)

#option-2
p="456,890,90"
COMMA=","
DOT="."
print(p.replace(COMMA,DOT))