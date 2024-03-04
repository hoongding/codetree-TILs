OFFSET = 1000
# M으로 못덮인 값 그냥 1 구하면 될듯

coors = [
    tuple(map(int, input().split())),
    tuple(map(int, input().split())),
    tuple(map(int, input().split()))
]

answer = [
    [0 for _ in range(OFFSET * 2 + 1)]
    for _ in range(OFFSET * 2 + 1)
]

for (index, (x1, y1, x2, y2)) in enumerate(coors):
    x1, y1 = x1 + OFFSET, y1 + OFFSET
    x2, y2 = x2 + OFFSET, y2 + OFFSET

    if index != 2:
        for row in range(x1, x2):
            for col in range(y1, y2):
                answer[col][row] += 1
    else:
        for row in range(x1, x2):
            for col in range(y1, y2):
                if answer[col][row] == 1:
                    answer[col][row] -= 1


area = 0
for row in answer:
    for box in row:
        if box == 1:
            area += 1

print(area)