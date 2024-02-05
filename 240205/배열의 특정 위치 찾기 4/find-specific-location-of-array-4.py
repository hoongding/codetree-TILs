numArr = list(map(int, input().split()))

cnt = 0
sum_num = 0

for num in numArr:
    if(num == 0):
        break
    if(num % 2 == 0):
        cnt = cnt + 1
        sum_num += num


print(cnt, sum_num)