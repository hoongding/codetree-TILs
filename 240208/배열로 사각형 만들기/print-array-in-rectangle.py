answer = [
    [1 for _ in range(5)]
    for _ in range(5) 
]

for row in range(1, 5):
    for col in range(1, 5):
        answer[row][col] = answer[row - 1][col] + answer[row][col - 1]

for line in answer:
    print(" ".join(map(str, line)))