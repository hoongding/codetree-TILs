# 가로 n 개 수열
# 세로 n 개 수열 중
# 연속해서 m 개 이상의 동일한 원소가 나오는 순간 이 존재하는 수열

n, m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 가로로 어떻게 탐색? 세로로 어떻게 탐색?

# 1. 가로 먼저 탐색!
answer = 0
for row in grid:
    cur_item = row[0]
    max_cnt = 0
    cnt = 1
    for idx in range(1, n):
        if row[idx] == cur_item:
            cnt += 1
        else:
            max_cnt = max(max_cnt, cnt)
            cnt = 1
            cur_item = row[idx]
    max_cnt = max(max_cnt, cnt)
    if max_cnt >= m:
        answer += 1
    
# 2. 세로 탐색
for i in range(n):
    cur_item = grid[0][i]
    cnt = 1
    max_cnt = 0
    for col in range(1, n):
        if grid[col][i] == cur_item:
            cnt += 1
        else:
            max_cnt = max(max_cnt, cnt)
            cnt = 1
            cur_item = grid[col][i]
    max_cnt = max(max_cnt, cnt)
    if max_cnt >= m:
        answer += 1

print(answer)