n = int(input())

nums = [
    int(input())
    for _ in range(n)
]

cnt = 1
cnts = []
for i in range(n):
    if i != 0 and nums[i] == nums[i - 1]:
        cnt += 1
    if i != 0 and nums[i] != nums[i - 1]:
        cnts.append(cnt)
        cnt = 1

print(max(cnts))