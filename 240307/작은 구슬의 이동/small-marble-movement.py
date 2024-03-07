n, t = tuple(map(int, input().split()))
row, col, direction = tuple(input().split())
row, col = int(row) - 1, int(col) - 1

directions = {
    'R': 0,
    'U': 1,
    'D': 2,
    'L': 3
}
# 1,0 0,1 0,-1 -1,0
dxs, dys = [1, 0, 0, -1], [0, -1, 1, 0]

def is_range(row, col):
    return row >= 0 and col >= 0 and row < n and col < n

cur_dir = directions[direction]
for _ in range(t):
    nx, ny = col + dxs[cur_dir], row + dys[cur_dir]
    if not is_range(nx, ny):
        cur_dir = 3 - cur_dir
    else:
        col = nx
        row = ny

print(row + 1, col + 1)