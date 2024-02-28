m1, d1, m2, d2 = tuple(map(int, input().split()))

days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

month, day = m1, d1
cnt = 0
while True:
    if month == m2 and day == d2:
        break

    cnt += 1
    day += 1
    
    if day > days[month]:
        month += 1
        day = 1

print(cnt + 1)