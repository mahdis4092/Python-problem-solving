season_number=int(input("Enter the season number"))
if season_number>=1 and season_number<=4:
    if season_number==1:
        print("Spring")
    elif season_number==2:
        print("Summer")
    elif season_number==3:
        print("Fall")
    else:
        print("winter")
else:
    print("Enter a valid number")