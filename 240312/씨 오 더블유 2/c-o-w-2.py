n = int(input())

strs = list(input())

cnt = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(i + 2, n):
            if strs[i] == 'C' and strs[j] == 'O' and strs[k] == 'W':
                cnt += 1

print(cnt)