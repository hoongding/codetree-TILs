[n, m] = list(map(int, input().split()))

answer = [
    [0 for _ in range(n)]
    for _ in range(n)
]

for _ in range(m):
    [x, y] = list(map(int, input().split()))
    answer[x - 1][y - 1] = 1

for line in answer:
    print(" ".join(map(str, line)))