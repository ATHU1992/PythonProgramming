N = int(input())
num_list = []
for i in range(N):
    command = input().split()
    if command[0].upper().strip() == "INSERT":
        num_list.insert(int(command[1]), int(command[2]))
    elif command[0].upper().strip() == "PRINT":
        print(num_list)
    elif command[0].upper().strip() == "REMOVE":
        num_list.remove(int(command[1]))
    elif command[0].upper().strip() == "APPEND":
        num_list.append(int(command[1]))
    elif command[0].upper().strip() == "SORT":
        num_list.sort()
    elif command[0].upper().strip() == "POP":
        num_list.pop()
    elif command[0].upper().strip() == "REVERSE":
        num_list.reverse()
