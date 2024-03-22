n, m = tuple(map(int, input().split()))

graph = [
    [0 for _ in range(n + 1)]
    for _ in range(n + 1)
]

visited = [False for _ in range(n + 1)]
vertex_cnt = 0

def dfs(vertex):
    global vertex_cnt

    for cur_v in range(1, n + 1):
        if graph[vertex][cur_v] and not visited[cur_v]:
            visited[cur_v] = True
            vertex_cnt += 1
            dfs(cur_v)

for i in range(m):
    v1, v2 = tuple(map(int, input().split()))
    graph[v1][v2], graph[v2][v1] = 1, 1

visited[1] = True
dfs(1)

print(vertex_cnt)