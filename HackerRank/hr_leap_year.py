def leap_year_check(year_check):
    if year_check % 4 == 0:
        if year_check % 100 != 0:
            return True
        else:
            if year_check % 400 == 0:
                return True
            else:
                return False
    else:
        return False


year = int(input("Enter an year :"))
check = leap_year_check(year)
if check:
    print("Leap year")
elif not check:
    print("Not Leap year")
