n = int(input("Enter the number"))

if n%2 == 1 :
    print("Wierd")
elif n%2 == 0 and n >= 2 and n <= 5 :
    print("Not Wierd")
elif n%2 == 0 and n >= 6 and n <= 20 :
    print("Wierd")
elif n%2 == 0 and n > 20 :
    print("Not Wierd")

