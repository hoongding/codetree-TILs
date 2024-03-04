n = int(input())
OFFSET = 100
class Square:
    def __init__(self, coors, idx):
        x1, y1, x2, y2 = coors
        self.x1 = x1 + OFFSET
        self.y1 = y1 + OFFSET
        self.x2 = x2 + OFFSET
        self.y2 = y2 + OFFSET
        if idx % 2 == 0:
            self.color = 'R'
        else:
            self.color = 'B'

squares = []
coors = [
    ['' for _ in range(OFFSET * 2 + 1)]
    for _ in range(OFFSET * 2 + 1)
]

for i in range(n):
    squares.append(Square(tuple(map(int, input().split())), i))

for square in squares:
    for col in range(square.y1, square.y2):
        for row in range(square.x1, square.x2):
            coors[col][row] = square.color

area = 0
for row in coors:
    for box in row:
        if box == 'B':
            area += 1

print(area)