# 2 2 1
# 최대 능력 최소 능력의 팀간의 능력 차이가 최소
import sys
# 모든 팀의 능력치가 서로 다르게 만들 수 없으면 - 1 ㄱㄱ
skills = list(map(int, input().split()))
skills.sort()
n = 5
# 1 2 3 4 5

min_sum = sys.maxsize
flag = False
for i in range(n):
    max_size = 0
    min_size = 0
    for j in range(n):
    # 첫번째 그룹만들기
        if i == j: continue
        temp_first_sum = skills[i] + skills[j]

        for k in range(n):
            if i == k or j == k: continue
            for l in range(n):
                if i == l or j == l or k == l: continue
                temp_second_sum = skills[k] + skills[l]
                # 두번째 그룹 만들기
            
                for m in range(n):
                    # 마지막 한명 선택
                    if m == i or m == j or m == k or m == l: continue
                    temp_third_sum = skills[m]

                    if temp_first_sum == temp_third_sum or temp_second_sum == temp_third_sum or temp_first_sum == temp_second_sum:
                        continue
                    else:
                        flag = True
                        max_size = max(temp_first_sum, temp_second_sum, temp_third_sum)
                        min_size = min(temp_first_sum, temp_second_sum, temp_third_sum)
                        min_sum = min(min_sum, max_size - min_size)

if not flag:
    print(-1)
else:
    print(min_sum)