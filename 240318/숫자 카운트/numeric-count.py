# 서로 다른 숫자 세개

n = int(input())

hints = [
    list(input().split())
    for _ in range(n)
]

for idx in range(n):
    num, first, second = hints[idx]
    num = list(map(int, list(num)))
    hints[idx] = [num, int(first), int(second)]

cnt = 0

for i in range(1, 10):
    for j in range(1, 10):
        if i == j: continue
        for k in range(1, 10):
            if i == k or j == k:
                continue
            
            all_hints = 0
            for (target, first, second) in hints:
                temp_first = 0
                temp_second = 0
                if i == target[0]:
                    temp_first += 1
                elif i in target: 
                    temp_second += 1

                if j == target[1]:
                    temp_first += 1
                elif j in target:
                    temp_second += 1

                if k == target[2]:
                    temp_first += 1
                elif k in target:
                    temp_second += 1
                
                if temp_first == first and temp_second == second:
                    all_hints += 1
            
            if all_hints == n:
                cnt += 1
                
print(cnt)