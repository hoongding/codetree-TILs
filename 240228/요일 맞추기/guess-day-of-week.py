m1, d1, m2, d2 = tuple(map(int, input().split()))

date = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
target_idx = 0

days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def get_days(month, day):
    m, d = 1, 1
    answer = 0
    while True:
        if m == month and d == day:
            break
        d += 1
        answer += 1

        if d == days[m]:
            d = 1
            m += 1

    return answer
    
        
m1_days = get_days(m1, d1)
m2_days = get_days(m2, d2)

difference = m2_days - m1_days

while difference < 0:
    difference += 7

print(date[difference % 7])