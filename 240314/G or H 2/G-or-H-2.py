import sys
n = int(input())

people = [
    tuple(input().split())
    for _ in range(n)
]

positions = []
for (position, _) in people:
    positions.append(int(position))

positions.sort()

max_size = - sys.maxsize
for i in range(len(positions)):
    for j in range(i, len(positions)):

        start_point, end_point = i, j

        g_cnt, h_cnt = 0, 0
        for (position, alphabet) in people:
            if positions[i] <= int(position) <= positions[j]:
                if alphabet == 'G': g_cnt += 1
                if alphabet == 'H': h_cnt += 1
            
        if g_cnt == h_cnt or (g_cnt > 0 and h_cnt == 0) or (h_cnt > 0 and g_cnt == 0):
            max_size = max(max_size, positions[j] - positions[i])

print(max_size)