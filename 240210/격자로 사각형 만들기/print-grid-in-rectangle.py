n = int(input())

answer = [
    [1 for _ in range(n)]
    for _ in range(n)
]

for row in range(1, n):
    for col in range(1, n):
        answer[row][col] = answer[row][col - 1] + answer[row - 1][col] + answer[row - 1][col - 1]
        

for line in answer:
    print(" ".join(map(str, line)))