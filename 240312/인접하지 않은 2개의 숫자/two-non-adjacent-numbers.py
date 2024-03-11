import sys
n = int(input())
nums = list(map(int, input().split()))

max_sum = -sys.maxsize
for i in range(n):
    for j in range(i + 2, n):
        max_sum = max(nums[i] + nums[j], max_sum)

print(max_sum)