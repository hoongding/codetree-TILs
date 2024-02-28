class Student:
    def __init__(self, h, w, num):
        self.h = h
        self.w = w
        self.num = num

n = int(input())
students = []

# 키가 작은 학생 앞으로, 키똑같으면 몸무게 큰학생 이 앞으로
for i in range(1, n + 1):
    h, w = tuple(map(int, input().split()))
    students.append(Student(h, w, i))

students.sort(key=lambda student: (student.h, -student.w))

for student in students:
    print(student.h, student.w, student.num)