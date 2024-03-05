n, m, k = tuple(map(int, input().split()))

nums = [
    int(input())
    for _ in range(m)
]

students = [0 for _ in range(m + 1)]

answer = -1
for num in nums:
    students[num] += 1
    if students[num] == k:
        answer = num
        break

print(answer)