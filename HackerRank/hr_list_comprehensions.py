x = int(input("x : "))
y = int(input("y : "))
z = int(input("z : "))
n = int(input("n : "))

output_list = [[a, b, c] for a in range(0, x + 1) for b in range(0, y + 1) for c in range(0, z + 1) if (a + b + c) != n]
print(output_list)
