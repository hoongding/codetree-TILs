n = int(input())

strs = list(input())

cnt = 0
for i in range(n):
    for j in range(i + 1, n ):
        for k in range(j + 1, n):
            if strs[i] == 'C' and strs[j] == 'O' and strs[k] == 'W':
                cnt += 1

print(cnt)