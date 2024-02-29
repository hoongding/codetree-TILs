m1, d1, m2, d2 = tuple(map(int, input().split()))
target_dow = input()

day_of_month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_of_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

cnt = 0
while True:
    if m1 == m2 and d1 == d2:
        break
    d1 += 1
    cnt += 1

    if d1 > day_of_month[m1]:
        m1 += 1
        d1 = 1

target_idx = 0
for index, day in enumerate(day_of_week):
    if day == target_dow:
        target_idx = index

if cnt - target_idx < 0:
    print(0)
else:
    print((cnt - target_idx) // 7 + 1)