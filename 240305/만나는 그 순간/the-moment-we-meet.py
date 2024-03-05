n, m = tuple(map(int, input().split()))

a_moves = [
    tuple(input().split())
    for _ in range(n)
]

b_moves = [
    tuple(input().split())
    for _ in range(m)
]

def make_trace(moves):
    trace = []
    place = 0
    for direction, move_time in moves:
        direction = 1 if direction == 'R' else -1
        move_time = int(move_time)
        for _ in range(move_time):
            trace.append(place)
            place += direction
    
    return trace

a_traces = make_trace(a_moves)
b_traces = make_trace(b_moves)

flag = False
for i in range(1, len(a_traces)):
    if a_traces[i] == b_traces[i]:
        print(i)
        flag = True
        break

if not flag:
    print(-1)