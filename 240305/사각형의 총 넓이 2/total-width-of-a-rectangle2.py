n = int(input())
OFFSET = 100

class Square:
    def __init__(self, coors):
        x1, y1, x2, y2 = coors
        self.x1 = x1 + OFFSET
        self.y1 = y1 + OFFSET
        self.x2 = x2 + OFFSET
        self.y2 = y2 + OFFSET
    
squares = [
    Square(tuple(map(int, input().split())))
    for _ in range(n)
]

answer = [
    [False for _ in range(OFFSET * 2 + 1)]
    for _ in range(OFFSET * 2 + 1)
]

for square in squares:
    for col in range(square.y1, square.y2):
        for row in range(square.x1, square.x2):
            answer[col][row] = True

area = 0

for row in answer:
    for box in row:
        if box:
            area += 1
print(area)