n, m = tuple(map(int, input().split()))

move_a = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

move_b = [
    tuple(map(int, input().split()))
    for _ in range(m)
]

winners = []

trace_a = []
distance_a = 0
# v, t 순서!
for v, t in move_a:
    for i in range(t):
        distance_a += v
        trace_a.append(distance_a)

trace_b = []
distance_b = 0
# v, t 순서!
for v, t in move_b:
    for i in range(t):
        distance_b += v
        trace_b.append(distance_b)

# 0 : A선두, 1: B선두, 2: A, B 선두
winner = -1
cnt = 0
for i in range(len(trace_a)):
    if trace_a[i] == trace_b[i]:
        if winner != 2:
            winner = 2
            cnt += 1
    elif trace_a[i] > trace_b[i]:
        if winner != 0:
            winner = 0
            cnt += 1
    else:
        if winner != 1:
            winner = 1
            cnt += 1

print(cnt)