weight = int(input("Enter your weight : "))
unit = input("Is your weight in Pounds(L) or Kilograms(K) : ")

if unit.upper() == "L":
    print("Your weight in Kgs : " + str(weight / 2.205))
elif unit.upper() == "K":
    print("Your weight in Lbs : " + str(weight * 2.205))