month=str(input("Enter the month"))
if month in ('January','March','May','July','August','October','December'):
    print(f"{month} has 31 days")
elif month in ('April','June','September','November'):
    print(f"{month} has 30 days")
else:
    print(f"{month} has 28 days")