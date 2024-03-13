n = int(input())

nums = list(map(int, input().split()))

cnt = 0
for i in range(n):
    for j in range(i, n):
        cur_sum = 0
        for idx in range(i, j + 1):
            cur_sum += nums[idx]

        avg = cur_sum / (j - i + 1)

        exists = False
        for idx in range(i, j + 1):
            if avg == nums[idx]:
                exists = True
        if exists:
            cnt += 1

print(cnt)