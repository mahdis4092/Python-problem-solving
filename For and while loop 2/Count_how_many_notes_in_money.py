def notes_count(amount):
    notes = [1000, 500, 100, 50, 10, 5, 1]
    count = [0, 0, 0, 0, 0, 0, 0]
    for i, note in enumerate(notes):
        if amount >= note:
            count[i] = amount // note
            amount = amount % note
    return count

amount = int(input("Enter amount: "))
count = notes_count(amount)
print("Number of 1000 notes:", count[0])
print("Number of 500 notes:", count[1])
print("Number of 100 notes:", count[2])
print("Number of 50 notes:", count[3])
print("Number of 10 notes:", count[4])
print("Number of 5 notes:", count[5])
print("Number of 1 notes:", count[6])
