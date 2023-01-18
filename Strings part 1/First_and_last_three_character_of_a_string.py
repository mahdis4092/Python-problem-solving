s="healthcaremedicine"
if len(s)<6:
    print("")
else:
    combine_string=s[0:3]+s[len(s)-3:]
    print(combine_string)
