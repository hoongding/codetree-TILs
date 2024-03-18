import sys
nums = list(map(int, input().split()))

nums.sort()
# 1 2 3 4 5 6

max_sum = -sys.maxsize
min_sum = sys.maxsize

for i in range(len(nums) // 2):
    temp_first = nums[i]
    temp_second = nums[len(nums) - 1 - i]

    max_sum = max(max_sum, temp_first + temp_second)
    min_sum = min(min_sum, temp_first + temp_second)

print(max_sum - min_sum)