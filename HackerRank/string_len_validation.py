name = input("Enter your name : ")

if len(name) < 3:
    print("Name field should be at least 3 characters long")
elif len(name) > 50:
    print("Name field should not be more than 50 characters")
else:
    print("Name field accepted")