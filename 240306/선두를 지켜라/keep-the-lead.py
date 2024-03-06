n, m = tuple(map(int, input().split()))

a_move = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

b_move = [
    tuple(map(int, input().split()))
    for _ in range(m)
]

total_time = 0
# v: 속도, t : 시간

a_trace = []
a_distance = 0
for speed, time in a_move:
    for i in range(time):
        a_distance += speed
        a_trace.append(a_distance)

b_trace = []
b_distance = 0
for speed, time in b_move:
    for i in range(time):
        b_distance += speed
        b_trace.append(b_distance)


lead = -1
answer = 0
for i in range(1, len(a_trace)):
    if a_trace[i] > b_trace[i]:
        if lead == 1:
            answer += 1
        lead = 0
    elif a_trace[i] < b_trace[i]:
        if lead == 0:
            answer += 1
        lead = 1

if answer == 0 and lead != -1:
    print(1)
else:      
    print(answer)