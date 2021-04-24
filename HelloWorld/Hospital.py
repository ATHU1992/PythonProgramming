from datetime import date
print('Hello Patient !')
print('* ' * 10)
name = input("Name of the patient : ")
birth_year = input("Birth year the patient : ")
is_admitted_before = input("Was the patient admitted before (Yes/No) : ")
print("-" * 20)
print("Name : " + name)
todays_date = date.today()
print(type(todays_date))
print("Age : " + str(todays_date.year - int(birth_year)))   #Need to convert it to String
if is_admitted_before == "No":
    print("Admission : New")
else:
    print("Admission : Old")
print("-" * 20)