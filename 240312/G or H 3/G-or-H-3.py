import sys
n, k = list(map(int, input().split()))

# 사진크기 k
# G가 찍히면 각각 1점, H찍히면 각각 2점
MAX_NUM = 10000
arr = [0] * (MAX_NUM + 1)
# 사람위치, 알파벳정보
for _ in range(n):
    x, c = tuple(input().split())
    x = int(x)
    
    arr[x] = 1 if c == 'G' else 2

max_size = -sys.maxsize

for i in range(MAX_NUM - k + 1):
    cur_score = 0
    for idx in range(k + 1):
        cur_score += arr[i + idx]
    max_size = max(max_size, cur_score)
    

print(max_size)