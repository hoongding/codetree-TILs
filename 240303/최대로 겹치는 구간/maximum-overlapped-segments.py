n = int(input())

arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

answer = [0 for _ in range(len(arr))]

for start, end in arr:
    for i in range(start - 1, end - 1):
        answer[i] += 1

print(answer)