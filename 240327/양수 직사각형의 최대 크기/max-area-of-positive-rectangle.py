n, m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

def is_range(x, y):
    return x >= 0 and y >= 0 and x < n and y < m

max_size = -1
for x in range(n):
    for y in range(m):
        start_point = (x, y)
        # 가로 1부터 n 까지 탐색
        # 세로크기 1부터 n 까지 탐색
        # 1, 1 이면 
        for row_size in range(0, n - x):
            for col_size in range(0, m - y):
                
                # row_size, col_size 정해졌으면 이제 탐색 시작
                flag = True
                for temp_x in range(x, x + row_size + 1):
                    for temp_y in range(y, y + col_size + 1):
                        if not is_range(temp_x, temp_y) or grid[temp_x][temp_y] <= 0:
                            flag = False
                            break
                if flag:
                    max_size = max(max_size, (row_size + 1) * (col_size + 1))

print(max_size)