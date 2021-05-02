n = int(input("Enter the number of students :"))
student_marks = {}
for _ in range(n):
    line = input().split()
    name, scores = line[0], line[1:]
    scores = map(float, scores)
    student_marks[name] = scores

query_name = input("Query : ")

marks = student_marks[query_name.strip()]
count = 0
sum_marks = 0.0
for i in marks:
    sum_marks = sum_marks + i
    count = count + 1
print("%.2f"%(sum_marks/count))
