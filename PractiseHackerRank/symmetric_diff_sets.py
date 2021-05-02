# if __name__ == '__main__':
M = int(input())
m_list = input().split()
N = int(input())
n_list = input().split()

m_list = map(int, m_list)
n_list = map(int, n_list)
m_set = set(m_list)
n_set = set(n_list)

a_set = m_set.difference(n_set)
b_set = n_set.difference(m_set)
result_set = a_set.union(b_set)
result_list = list(result_set)

sorted_list = sorted(result_list)

for i in sorted_list:
    print(i)
