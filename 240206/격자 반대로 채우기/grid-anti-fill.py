n = int(input())

answer = [
    [0 for _ in range(n)]
    for _ in range(n)   
]

count = 1

direction = n % 2

for col in range(n - 1, -1, -1):
    if (col + 1) % 2 == direction:
        for row in reversed(range(n)):
            answer[row][col] = count
            count += 1
    else:
        for row in range(n):
            answer[row][col] = count
            count += 1

for line in answer:
    print(" ".join(map(str, line)))