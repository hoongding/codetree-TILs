day, hour, minute = tuple(map(int, input().split()))

if (day == 11 and hour < 11) or (day == 11 and hour == 11 and minute < 11):
    print(-1)

cnt = 0
t_d, t_h, t_m = (11, 11, 11)
while True:
    if t_d == day and t_h == hour and t_m == minute:
        break
    
    cnt += 1
    t_m += 1

    if t_m == 60:
        t_h += 1
        t_m = 0
    if t_h == 24:
        t_d += 1
        t_h = 0

print(cnt)