price_of_home = 1000000
buyer_credit = int(input("Enter your credit score : "))
buyer_income = int(input("Enter your yearly income : "))
has_criminal_record = input("Do you have a criminal record (True/False) : ")
print(has_criminal_record)
if buyer_credit > 170 and buyer_income > 50000 and has_criminal_record != False:
    print("You have to pay {} as down-payment".format(0.1 * price_of_home))
else:
    print("You have to pay {} as down-payment".format(0.2 * price_of_home))
