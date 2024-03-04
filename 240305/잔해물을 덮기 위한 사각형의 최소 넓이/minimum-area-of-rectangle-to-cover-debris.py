f_x1, f_y1, f_x2, f_y2 = tuple(map(int, input().split()))
s_x1, s_y1, s_x2, s_y2 = tuple(map(int, input().split()))

OFFSET = 1000

coor = [
    [0 for _ in range(OFFSET * 2  + 1)]
    for _ in range(OFFSET * 2  + 1)
]

for row in range(f_x1 + OFFSET, f_x2 + OFFSET + 1):
    for col in range(f_y1 + OFFSET, f_y2 + OFFSET + 1):
        coor[col][row] += 1

for row in range(s_x1 + OFFSET, s_x2 + OFFSET + 1):
    for col in range(s_y1 + OFFSET, s_y2 + OFFSET + 1):
        coor[col][row] -= 1

rest_area_x = []
rest_area_y = []
for col in range(OFFSET * 2 + 1):
    for row in range(OFFSET * 2 + 1):
        if coor[col][row] == 1:
            rest_area_x.append(row)
            rest_area_y.append(col)
if len(rest_area_x) == 0:
    print(0)
else:
    min_x, max_x = min(rest_area_x), max(rest_area_x)
    min_y, max_y = min(rest_area_y), max(rest_area_y)
    print((max_x - min_x) * (max_y - min_y))