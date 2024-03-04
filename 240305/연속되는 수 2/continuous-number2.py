n = int(input())

nums = [
    int(input())
    for _ in range(n)
]

cnt = 1
for i in range(n):
    if i != 0 and nums[i] != nums[i - 1]:
        cnt += 1

print(cnt)