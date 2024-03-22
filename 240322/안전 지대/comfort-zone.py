# 안잠기는 곳이 필요!!!
n, m = tuple(map(int, input().split()))


# 마을 지도
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

def is_range(x, y):
    return x >= 0 and y >= 0 and x < n and y < m

def can_go(x, y):
    if not is_range(x, y):
        return False
    if visited[x][y] or temp_grid[x][y] == 0:
        return False
    return True

def dfs(x, y):
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if can_go(new_x, new_y):
            visited[new_x][new_y] = True
            dfs(new_x, new_y)

# 안전 구역이 최대개수가 될때의 K, 안전영역 수 출력
# 최대 K가 여러개라면 가장 작은 K 뽑기
max_order = 0
min_k = 101
for k in range(1, 101):
    temp_grid = [
        [0 for _ in range(m)]
        for _ in range(n)
    ]
    visited = [
        [False for _ in range(m)]
        for _ in range(n)
    ]

    # temp_grid 채우기
    for x in range(n):
        for y in range(m):
            if k < grid[x][y]:
                temp_grid[x][y] = grid[x][y]
    order = 0
    for i in range(n):
        for j in range(m):
            if can_go(i, j):
                dfs(i, j)
                order += 1

    if max_order < order:
        max_order = max(max_order, order)
        min_k = k


if max_order == 0:
    print(1, 0)
else:
    print(min_k, max_order)