student_num = int(input())

students_scores = []

for _ in range(student_num):
    students_scores.append(list(map(int, input().split())))

def get_average(student_scores):
    return sum(student_scores) / 4

pass_students = 0

for student_scores in students_scores:
    average = get_average(student_scores)
    if average >= 60:
        print('pass')
        pass_students += 1
    else:
        print('fail')

print(pass_students)