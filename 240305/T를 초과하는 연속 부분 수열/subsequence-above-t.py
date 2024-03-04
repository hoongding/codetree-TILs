(n, t) = tuple(map(int, input().split()))

nums = list(map(int, input().split()))

cnt, ans = 0, 0

for i in range(n):
    if i != 0 and nums[i] > t:
        cnt += 1
    elif i != 0 and nums[i] <= t:
        cnt = 1
    ans = max(cnt, ans)

print(ans)