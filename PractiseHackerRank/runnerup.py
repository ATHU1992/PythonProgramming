n = int(input("Enter the number of candidates :"))
arr = map(int, input("Enter all the scores :").split())
sort_arr = sorted(arr, reverse=True)
print(list(sort_arr))
winner = sort_arr[0]
runner = sort_arr[0]
for i in sort_arr:
    if i < winner:
        runner = i
        break
    elif i == winner:
        continue

print(runner)

# Best Solution :
# n = int(input())
# a = sorted(map(int, input().split()), reverse=True)
# print(a[a.count(a[0])])
