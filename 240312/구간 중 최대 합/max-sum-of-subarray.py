import sys

n, k = list(map(int, input().split()))
nums = list(map(int, input().split()))

max_sum = -sys.maxsize
for i in range(n - k + 1):
    cur_sum = 0
    for j in range(k):
        cur_sum += nums[i + j]
    max_sum = max(max_sum, cur_sum)

print(max_sum)