n = int(input())

MAX_TRIAL = 1000
MAX_MOVE = 100
MAX_LEN = MAX_TRIAL * MAX_MOVE * 2

arr = [
    tuple(input().split())
    for _ in range(n)
]

class Tile:
    def __init__(self, white, black, cur_col):
        self.white = white
        self.black = black
        self.cur_col = cur_col
    
    def get_color(self):
        return self.cur_col
    
    def set_color(self, color):
        
        if cmd == 'L':
            self.white += 1
            self.cur_col = 'W'
        if color == 'R':
            self.black += 1
            self.cur_col = 'B'
        if self.white >= 2 and self.black >= 2:
            self.cur_col = 'G'
        

answer = [ Tile(0, 0, '') for _ in range(MAX_LEN) ]
start = MAX_LEN // 2

for move, cmd in arr:
    
    direction = 1 if cmd == 'R' else -1
    move = int(move) * direction

    for i in range(start, start + move, direction):
        answer[i].set_color(cmd)
    start = start + move - direction
    

w_cnt = 0
b_cnt = 0
g_cnt = 0

for tile in answer:
    tile_col = tile.get_color()
    if tile_col == 'W': w_cnt += 1
    elif tile_col == 'B': b_cnt += 1
    elif tile_col == 'G': g_cnt += 1


print(w_cnt, b_cnt, g_cnt)