# T개의 알파벳, S, N으로만 주어진다.
# 특정위치 k로부터 가장 가까이 있는 알파벳 S까지의 거리 d1
# k로부터 가장 가까이에 있는 알파벳 N까지거리 d2 
# d1 <= d2 -> k는 특별한 위치!
# a <= k <= b
t, a, b = tuple(map(int, input().split()))

points = [
    tuple(input().split())
    for _ in range(t)
]

cnt = 0
for k in range(a, b + 1):
    min_d1, min_d2 = 10000, 10000

    for alphabet, point in points:
        point = int(point)
        if alphabet == 'S':
            min_d1 = min(min_d1, abs(point - k))
        elif alphabet == 'N':
            min_d2 = min(min_d2, abs(point - k))
    
    if min_d1 <= min_d2:
        cnt += 1

print(cnt)