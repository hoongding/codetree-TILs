n = int(input())
OFFSET = 100

arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

answer = [0 for _ in range(202)]

for start, end in arr:
    for i in range(start - 1 + OFFSET, end - 1 + OFFSET):
        answer[i] += 1

print(max(answer))