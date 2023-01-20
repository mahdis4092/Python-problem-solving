import string
s="The quick brown fox jumps over the lazy dog"
SPACE=" "
s_set=set(s.lower())
if SPACE in s_set:
    s_set.remove(SPACE)
if s_set == set(string.ascii_lowercase):
        print(True)
else:
    print(False)







