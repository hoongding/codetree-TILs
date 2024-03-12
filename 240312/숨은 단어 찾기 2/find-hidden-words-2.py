n, m = list(map(int, input().split()))

target = ['L', 'E', 'E']
grid = [
    list(input())
    for _ in range(n)
]

dxs, dys = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]

def is_range(row, col):
    return row >= 0 and col >= 0 and row < n and col < m


cnt = 0
for i in range(n):
    for j in range(m):

        if grid[i][j] == 'L':
            for dx, dy in zip(dxs, dys):
                cur_idx = 1
                cur_i = i
                cur_j = j
                while cur_idx <= 3:
                    if cur_idx == 3:
                        cnt += 1
                        break
                    nx = cur_i + dx
                    ny = cur_j + dy
                    if not is_range(nx, ny):
                        break
                    if grid[nx][ny] != target[cur_idx]:
                        break
                    if grid[nx][ny] == target[cur_idx]:
                        cur_idx += 1
                    
                    cur_i = nx
                    cur_j = ny

print(cnt)