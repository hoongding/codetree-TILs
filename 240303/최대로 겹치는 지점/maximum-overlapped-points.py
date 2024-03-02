n = int(input())
arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

answer = [0 for _ in range(101)]

for start, end in arr:
    for n in range(start - 1, end):
        answer[n] += 1

print(max(answer))