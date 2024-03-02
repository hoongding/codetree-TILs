n = int(input())
OFFSET = 1000
start = 1000
cmds = [
    tuple(input().split())
    for _ in range(n)
]

answer = [0 for _ in range(OFFSET * 2)]

for x, direction in cmds:
    x = int(x) if direction == 'R' else (int(x) * (-1))
    temp_start = start if x > 0 else (start + x)
    end = (start + x) if x > 0 else start
    start = end if x > 0 else temp_start
    
    for idx in range(temp_start, end):
        answer[idx] += 1
    

cnt = 0

for i in answer:
    if i >= 2:
        cnt += 1

print(cnt)