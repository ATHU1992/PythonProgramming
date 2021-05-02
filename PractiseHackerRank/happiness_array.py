# if __name__ == '__main__':
M = input().split()
x_list = map(int, input().split())
a_list = input().split()
b_list = input().split()
happiness_var = 0
a_set = set(map(int, a_list))
b_set = set(map(int, b_list))

for i in x_list:
    if i in a_set:
        happiness_var = happiness_var + 1
    elif i in b_set:
        happiness_var = happiness_var - 1

print(happiness_var)
