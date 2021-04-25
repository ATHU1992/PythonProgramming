numbers = [22, 45, 55, 1, 33, 0, 2, 2, 4, 22, -11, 333, 333, 849, 44, 22, 22, 22]
unique = []
for number in numbers:
    if number not in unique:
        unique.append(number)

print(unique)
