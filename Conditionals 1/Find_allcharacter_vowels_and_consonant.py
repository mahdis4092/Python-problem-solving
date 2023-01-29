'''
given_string='Score: 36'
new_str=given_string.lower()
print(new_str)
for elem in new_str:
    if elem=='a'or elem=='e'or elem=='i'or elem=='o'or elem=='u':
        print(f"{elem} is a vowels".format(elem))
    elif elem==" " or elem==":":
        print(f"{elem} is none".format(elem))
    else:
        print(f"{elem} is consonant".format(elem))
        '''
#given solution-more accurate
text='Score: 36'
if not text:
    print("empty string")
else:
    for char in text.lower():
        if char in ('a','e','i','o','u'):
            print(f"{char} is a vowels")
        elif not char.isalpha():  #alpha means alphabetical or letters
            print(f"{char} is not a letter")
        else:
            print(f"{char} is a consonant")

