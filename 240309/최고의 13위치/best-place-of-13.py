import sys
n = int(input())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
# 3 <= n <= 20
max_size = -sys.maxsize
for row in range(0, n - 2):
    for col in range(n):
        cnt = 0
        if grid[col][row] == 1:
            cnt += 1
        if grid[col][row + 1] == 1:
            cnt += 1
        if grid[col][row + 2] == 1:
            cnt += 1
        
        max_size = max(max_size, cnt)

print(max_size)