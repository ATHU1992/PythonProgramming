prices = [10, 20, 34, 34, 33, 64, 222]
total_price = 0
for item_price in prices:
    total_price = total_price + item_price

print(total_price)

for x in range(4):
    for y in range(4):
        print(f"({x},{y})")

numbers = [5, 5, 6, 2, 3, 1]

for i in numbers:
    #   for j in range(i):
    print("*" * i)

for i in numbers:
    print()
    for j in range(i):
        print("*", end="")
