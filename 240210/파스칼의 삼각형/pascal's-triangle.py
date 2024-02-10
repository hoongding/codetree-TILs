n = int(input())

## (i, j) = (i - 1, j - 1) + (i - 1) + (j)

answer = [
    [1 for _ in range(row)]
    for row in range(1, n + 1)
]

if(n >= 3):
    for row in range(2, n):
        for col in range(1, row):
            answer[row][col] = answer[row - 1][col - 1] + answer[row - 1][col]

for line in answer:
    print(" ".join(map(str, line)))