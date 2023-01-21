#my solution not complete
'''
p="Hello World"
new_p=""
space=" "
#p_split=p.split()
for char in p:
    if char!=" ":
        new_p+=p[::-1]
        new_p.swapcase()
        print(new_p)
'''
#option-2
s = "Hello World"

words_list = s.split(" ")
new_s = ""

for word in words_list:
	 reversed_word = word[::-1]
	 swapped_case = reversed_word.swapcase()
	 new_s += swapped_case + " "

new_s.rstrip()

print(new_s)