n = int(input())

nums = list(map(int, input().split()))

nums_with_idx = []
for (index, num) in enumerate(nums):
    nums_with_idx.append((num, index + 1))

answer = [ 0 for _ in range(n) ]
sort_arr = sorted(nums_with_idx, key=lambda num: (num[0], num[1]))

for (idx, (_, index)) in enumerate(sort_arr):
    answer[index - 1] = idx + 1 


for idx in answer:
    print(idx, end=" ")