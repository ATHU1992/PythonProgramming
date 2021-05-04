# if __name__ == '__main__':
stamp_set = set()
number_of_countries = int(input())
for i in range(number_of_countries):
    stamp_set.add(input().upper().strip())

print(len(stamp_set))
print(list(stamp_set))
