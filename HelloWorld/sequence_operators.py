computer = ["Keyboard", "Mouse", "CPU", "GPU"]

for i in range(0, 4):
    print(computer[i])

for i in computer:
    print(i)


age = 24
#These are replacement fields
print("My age is {0} years".format(age))
print("There are {0} days in {1},{2},{3},{4},{5},{6},{7} and {8}".format(31, "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug"))

print("""
Jan : {2}
Feb : {0}
Mar : {2}
Apr : {1}
May : {2}
Jun : {1}
Jul : {2}
Aug : {2}
Sep : {1}
Oct : {2}
Nov : {1}
Dec : {2}
""".format(28, 30, 31))


for i in range(1, 13):
    print("Number {0} squared is {1} and cubed is {2}".format(i, i**2, i**3))

#For formatting -
for i in range(1, 12):
    print("Number {0:2} squared is {1:4} and cubed is {2:4}".format(i, i**2, i**3))
#Left aligned and center aligned
for i in range(1, 12):
    print("Number {0:<2} squared is {1:<4} and cubed is {2:^4}".format(i, i**2, i**3))
print("1Value of Pi is {0}".format(22/7))
print("2Value of Pi is {0:12}".format(22/7))
print("3Value of Pi is {0:12f}".format(22/7))
print("4Value of Pi is {0:12.50f}".format(22/7))
print("5Value of Pi is {0:52.50f}".format(22/7))
print("6Value of Pi is {0:62.50f}".format(22/7))
print("7Value of Pi is {0:72.54f}".format(22/7))

#f-string
age_in_words = "28 years"
name = "Atharva"
print(f"Hi {name}, your age is {age_in_words}")

print(f"Value of pi is {22/7:12.50f}")

for i in range(1, 20):
    for j in range(1,i):
        print("*",end="")
    print()