n, m = tuple(map(int, input().split()))

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [False for _ in range(n)]
    for _ in range(m)
]

order = 1

def is_range(x, y):
    return x >= 0 and y >= 0 and x <= n - 1 and y <= m - 1

def can_go(x, y):
    if not is_range(x, y):
        return False
    if visited[x][y] or grid[x][y] == 0:
        return False
    
    return True

def dfs(x, y):
    global order

    dxs, dys = [1, 0], [0, 1]

    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy

        if can_go(new_x, new_y):
            grid[new_x][new_y] = order
            order += 1
            visited[new_x][new_y] = True
            dfs(new_x, new_y)


grid[0][0] = order
order += 1
visited[0][0] = True
dfs(0, 0)

if grid[n - 1][m - 1] != 1:
    print(1)
else:
    print(0)