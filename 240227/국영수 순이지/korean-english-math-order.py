n = int(input())
student_arr = [
    tuple(input().split())
    for _ in range(n)
]

student_arr.sort(key=lambda x: (-int(x[1]), -int(x[2]), -int(x[3])))

for student in student_arr:
    name, kor, eng, math = student
    print(name, kor, eng, math)