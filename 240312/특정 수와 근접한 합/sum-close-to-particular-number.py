import sys

n, target = list(map(int, input().split()))
nums = list(map(int, input().split()))

# 정확히 2개 제외해서 n-2개의 합이 s와 가까운것
min_difference = sys.maxsize

for i in range(n):
    for j in range(i + 1, n):
        
        cur_sum = 0
        for idx in range(n):
            if idx != i and idx != j:
                cur_sum += nums[idx]
        
        difference = abs(target - cur_sum)
        
        min_difference = min(difference, min_difference)

print(min_difference)