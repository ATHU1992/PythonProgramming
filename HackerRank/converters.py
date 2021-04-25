def find_largest_number(numbers):
    largest_number = numbers[0]
    list_length = len(numbers)
    for i in range(list_length):
        if numbers[i] > largest_number:
            largest_number = numbers[i]
    return largest_number
