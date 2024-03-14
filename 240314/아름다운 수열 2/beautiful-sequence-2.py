n, m = tuple(map(int, input().split()))

a_arr = list(map(int, input().split()))
b_arr = list(map(int, input().split()))


cnt = 0

for i in range(n - m + 1):
    temp_arr = []
    for idx in range(m):
        if a_arr[i + idx] in b_arr:
            temp_arr.append(a_arr[i + idx])
    
    if len(list(set(temp_arr))) == m:
        cnt += 1

print(cnt)