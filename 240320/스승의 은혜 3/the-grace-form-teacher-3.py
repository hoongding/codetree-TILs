n, budget = tuple(map(int, input().split()))

# 선생님은 선물 하나를 정해서 반값으로 할인받을 수 잇는 쿠폰이 있음
students = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 선물의가격, 배송비
max_students = 0
for i in range(n):
    [a, b] = students[i]

    temp_arr = [
        students[j][0] + students[j][1]
        for j in range(n)
    ]
    temp_arr[i] = a // 2 + b
    temp_arr.sort()
    temp_sum, cnt = 0, 0
    for idx in range(n):
        temp_sum += temp_arr[idx]
        
        if temp_sum <= budget:
            cnt += 1
    max_students = max(max_students, cnt)


print(max_students)