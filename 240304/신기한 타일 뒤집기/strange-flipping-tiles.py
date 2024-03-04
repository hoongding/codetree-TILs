n = int(input())

arr = [
    tuple(input().split())
    for _ in range(n)
]
MAX_LEN = 100000

class Tile:
    def __init__(self, cur_col):
        self.cur_col = cur_col
    def set_col(self, direction):
        if direction == 'L':
            self.cur_col = 'W'
        elif direction == 'R':
            self.cur_col = 'B'

answer = [Tile('') for _ in range(MAX_LEN * 2 + 1)]

start = MAX_LEN // 2 + 1
for move, cmd in arr:
    direction = 1 if cmd == 'R' else -1
    move = int(move) * direction

    for i in range(start, start + move, direction):
        answer[i].set_col(cmd)
    start = start + move - direction

w_cnt = 0
b_cnt = 0

for tile in answer:
    if tile.cur_col == 'W':
        w_cnt += 1
    elif tile.cur_col == 'B':
        b_cnt += 1
    
print(w_cnt, b_cnt)