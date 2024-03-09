import sys
n = int(input())

position = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

min_val = sys.maxsize
x, y = position[0]

for i in range(1, len(position) - 1):
    # i가 거를 번호!!
    distance = 0
    for j in range(1, len(position)):
        if i == j:
            continue
        else:
            n_x, n_y = position[j]
            distance += abs(n_x - x) + abs(n_y - y)
            x, y = n_x, n_y
        
    x, y = position[0]
    min_val = min(distance, min_val)

print(min_val)