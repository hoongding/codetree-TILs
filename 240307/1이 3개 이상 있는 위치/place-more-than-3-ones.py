n = int(input())

square = [
    list(map(int, input().split()))
    for _ in range(n)
]

def is_range(x, y):
    return x >= 0 and y >= 0 and x < len(square) and y < len(square)
# 0, 1  1, 0   0, -1  -1, 0
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

answer = 0
for col in range(len(square)):
    for row in range(len(square)):
        cnt = 0
        for nx, ny in zip(dxs, dys):
            if is_range(col + nx, row + ny) and square[col + nx][row + ny] == 1:
                cnt += 1
        if cnt >= 3:
            answer += 1


print(answer)