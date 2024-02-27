n = int(input())

class Student:
    def __init__(self, h, w, index):
        self.h = h
        self.w = w
        self.index= index


students = []

for idx in range(1, n + 1):
    h, w = tuple(map(int, input().split()))
    students.append(Student(h, w, idx))

# 키가 더큰 학생이 앞
# 키가 똑같으면 몸무게가 더 큰 학생
# 다음은 번호가 작은 학생

students.sort(key=lambda person: (-person.h, -person.w, person.index))

for student in students:
    print(student.h, student.w, student.index)