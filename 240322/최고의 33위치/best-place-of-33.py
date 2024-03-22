n = int(input())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

def is_range(x, y):
    return x + 2 >= n or y + 2 >= n


max_cnt = 0
# 제일 왼쪽 점 잡기
for x in range(n):
    for y in range(n):
        if not is_range(x, y):
            temp_cnt = 0
            for temp_x in range(x, x + 3):
                for temp_y in range(y, y + 3):
                    if grid[temp_x][temp_y] == 1:
                        temp_cnt += 1
            max_cnt = max(max_cnt, temp_cnt) 


print(max_cnt)