import sys

n, k = list(map(int, input().split()))
nums = list(map(int, input().split()))

max_sum = -sys.maxsize
for i in range(n - k + 1):
    max_sum = max(max_sum, nums[i] + nums[i + 1] + nums[i + 2])

print(max_sum)