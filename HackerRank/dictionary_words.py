numbers_to_words = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero",
}

phone_number = str(input("Enter your number"))
phone_number_in_words = ""
for digit in phone_number:
    phone_number_in_words = phone_number_in_words + " " + numbers_to_words.get(digit, "!")

print(phone_number_in_words)
