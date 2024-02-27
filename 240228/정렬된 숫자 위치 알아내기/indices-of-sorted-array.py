n = int(input())

nums = list(map(int, input().split()))

nums_with_idx = []
for (index, num) in enumerate(nums):
    nums_with_idx.append((num, index + 1))

sort_arr = sorted(nums_with_idx, key=lambda num: (num[0], num[1]))

def find_idx(target):
    for (index, (num, _)) in enumerate(sort_arr):
        if target == num:
            return index + 1

change_idx = []
for num, index in nums_with_idx:
    if find_idx(num) in change_idx:
        change_idx.append(find_idx(num) + 1)        
    else: change_idx.append(find_idx(num))

for idx in change_idx:
    print(idx, end=" ")