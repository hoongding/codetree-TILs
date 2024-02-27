n = int(input())
# (x1, y1), (x2, y2) = |x1 - x2| + |y1 - y2|

class Point:
    def __init__(self, x, y, index):
        if x < 0:
            x = -x
        if y < 0:
            y = -y

        self.distance = x + y
        self.index = index

points = []

for idx in range(1, n + 1):
    [x, y] = list(map(int, input().split()))
    points.append(Point(x, y, idx))

points.sort(key=lambda point: (point.distance, point.index))

for point in points:
    print(point.index)