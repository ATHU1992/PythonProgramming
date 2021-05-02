# students1 = []
# for _ in range(int(input("Number of students :"))):
#    name = input("Name :")
#    score = float(input("Score :"))
#    students1.append([name, score])
# print(students1)
students = [['Atharva', 32.0], ['Uma', 32.8], ['Mangesh', 32.0], ['Tejashri', 32.8], ['Ameya', 32.0],
            ['Suman', 32.8]]
list_marks = []
for i in range(len(students)):
    if students[i][1] not in list_marks:
        list_marks.append(students[i][1])
list_marks.sort()
result_list = []
for i in range(len(students)):
    if students[i][1] == list_marks[1]:
        result_list.append(students[i])

sorted_result = sorted(result_list)
for i in range(len(sorted_result)):
    print(sorted_result[i][0])
