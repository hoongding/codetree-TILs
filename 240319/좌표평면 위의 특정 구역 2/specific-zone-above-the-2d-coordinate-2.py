import sys

n = int(input())

points = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

min_area = sys.maxsize
for i in range(len(points)):
    max_x, min_x = -sys.maxsize, sys.maxsize
    max_y, min_y = -sys.maxsize, sys.maxsize
    for (idx, (x, y)) in enumerate(points):
        if i == idx: continue
        max_x, min_x = max(max_x, x), min(min_x, x)
        max_y, min_y = max(max_y, y), min(min_y, y)

    min_area = min(min_area, (max_x - min_x) * (max_y - min_y))

print(min_area)