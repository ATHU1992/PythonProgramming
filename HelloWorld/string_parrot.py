parrot = "Norwegian Blue"
#         01234567890123
print(parrot[0:4])
print(parrot[4:])
print(parrot[:4])
print(parrot[:])
print()
print(parrot[1:-4])
print()
print(parrot[-1:1])
print()
print(parrot[3])
print(parrot[-6])

print(parrot[1:12:2])

print('*' * 15)
alphabets = "abcdefghijklmnopqrstuvwxyz"
#back_alphabets = alphabets[25:0:-1]
#print(back_alphabets)
#back_alphabets = alphabets[25:-27:-1]
#print(back_alphabets)
print(alphabets[16:13:-1])
print(alphabets[4::-1])
print(alphabets[25:17:-1])
print('*' * 15)

print('-' * 15)
print(parrot[::-1])
print('-' * 15)

first_name = "Atharva"
last_name = "Kekare"
message = first_name + ' [' + last_name + '] is a coder'
formatted_message = f'{first_name} [{last_name}] is a coder'

print(message)
print(formatted_message)
print(formatted_message.upper())
print(formatted_message.lower())
print(formatted_message.find('[' ))
print(formatted_message.replace('Atharva', 'Atharva the great'))
print(formatted_message.title())
print('Kekare' in formatted_message)

number = "9,123;234:123 123,775;236"
seperators = number[1::4]
print(seperators)

values = "".join(char if char not in seperators else "  " for char in number).split()
print([int(val) for val in values])