n, m = tuple(map(int, input().split()))

square = [
    [False] * n
    for _ in range(n)
]

cmds = [
    tuple(map(int, input().split()))
    for _ in range(m)
]

# 0,1 1,0 0,-1 -1,0
dxs, dyx = [0, 1, 0, -1], [1, 0, -1, 0]

def is_range(col, row):
    return col >= 0 and row >= 0 and col < n and row < n

for x, y in cmds:
    x, y = x - 1, y - 1
    square[x][y] = True
    cnt = 0
    for dx, dy in zip(dxs, dyx):
        if is_range(x + dx, y + dy) and square[x + dx][y + dy]:
            cnt += 1
    
    if cnt == 3:
        print(1)
    else:
        print(0)