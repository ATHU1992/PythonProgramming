numbers = [23, 45, 55, 1, 33, 0, 2, 22, -11, 333, 849]
largest_number = numbers[0]
list_length = len(numbers)
for i in range(list_length):
    if numbers[i] > largest_number:
        largest_number = numbers[i]
print(f"Largest Number : {largest_number}")

#Other String functions :

numbers = [22, 45, 55, 1, 33, 0, 2, 22, -11, 333, 849, 44, 22, 22, 22]
numbers.insert(0, 55)
print(numbers)
numbers.remove(-11)
print(numbers)
numbers.pop()
print(numbers)
print(numbers.sort())
print(numbers)
numbers.reverse()
print(numbers)
print(numbers.index(333))
print(333 in numbers)
print(numbers.count(22))
numbers.clear()
print(numbers)