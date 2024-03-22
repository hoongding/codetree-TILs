from collections import Counter
n = int(input())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [0 for _ in range(n)]
    for _ in range(n)
]

# 0이 일단 벽, 벽으로 둘러쌓여 있으면 같은 마을에 잇는 사람들.



def is_range(x, y):
    return x >= 0 and y >= 0 and x < n and y < n

def can_go(x, y):
    if not is_range(x, y):
        return False
    if grid[x][y] == 0 or visited[x][y] != 0:
        return False
    return True

# 마을에 있는 주민 수 넣을거임

people = 1
def dfs(x, y):
    global people
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if can_go(new_x, new_y):
            visited[new_x][new_y] = people
            dfs(new_x, new_y)

for i in range(n):
    for j in range(n):
        if grid[i][j] != 0 and visited[i][j] == 0:
            visited[i][j] = people
            dfs(i, j)
            people += 1

answer = []
for i in range(n):
    for j in range(n):
        if visited[i][j] != 0:
            answer.append(visited[i][j])

print(len(set(answer)))

answer = Counter(answer)
answer.most_common()

counts = []

for count in answer:
    counts.append(answer[count])

counts.sort()

for count in counts:
    print(count)