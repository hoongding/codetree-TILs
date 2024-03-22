n = int(input())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [False for _ in range(n)]
    for _ in range(n)
]

# 상하좌우로 인접한 칸끼리 같은숫자 면 하나의 블럭! 
# 블럭 칸수 4개이상이면 터짐

# 터지게 되는 블럭 수, 최대 블럭의 크기 구해라

def is_range(x, y):
    return x >= 0 and y >= 0 and x < n and y < n

def can_go(x, y):
    if not is_range(x, y):
        return False
    if visited[x][y]:
        return False
    if target != grid[x][y]:
        return False
    return True

def dfs(x, y):
    global order, target
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    for dx, dy in directions:
        new_x = x + dx
        new_y = y + dy
        if can_go(new_x, new_y):
            visited[new_x][new_y] = True
            order += 1
            dfs(new_x, new_y)


answer = []
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            target = grid[i][j]
            visited[i][j] = True
            order = 1
            dfs(i, j)
            if order >= 4:
                answer.append((grid[i][j], order))

answer.sort(lambda x: x[1])

print(len(answer), answer[-1][1])