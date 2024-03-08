n = int(input())

# n 남쪽, 2n 서쪽, 3n 북쪽, 4n 동쪽

# / : (1, 0) <-> (0, 1)  (-1, 0) <-> (0, -1)
# 0 3    1 2

# \ : (1, 0) <-> (0, -1)  (-1, 0) <-> (0, 1)
# 0 2     1 3

# 1,0  -1,0  0,-1  0,1

dxs, dys = [1, -1, 0, 0], [0, 0, -1, 1]

def is_range(n_row, n_col):
    return n_row >= 0 and n_col >= 0 and n_row < n and n_col < n

mirrors = [
    list(input())
    for _ in range(n)
]
# / \\
cnt = 0
s_pos = int(input()) - 1

# [s_pos = 0 ~ n - 1]  (0, s_pos) // [s_pos = n ~ 2n - 1] ((s_pos) % n , n - 1) 
# 2n + 1 ~ 3n ((n - 1), ((n - 1) - ((s_pos) % n)) // 3n+1 ~ 4n ( ((n - 1) - ((s_pos) % n)), 0)

def make_s(s_pos):
    if s_pos // n == 0:
        return (0, s_pos, 0)
    elif s_pos // n == 1:
        return (s_pos % n , n - 1, 2)
    elif s_pos // n == 2:
        return (n - 1, (n - 1) - (s_pos % n), 1)
    else:
        return (((n - 1) - s_pos % n), 0, 3)

cur_x, cur_y, cur_dir = make_s(s_pos)
cnt = 0

while True:
    if mirrors[cur_x][cur_y] == '/':
        n_x, n_y, n_dir = cur_x + dxs[cur_dir], cur_y + dys[cur_dir], (3 - cur_dir)
    else:
        n_x, n_y, n_dir = cur_x + dxs[cur_dir], cur_y + dys[cur_dir], ((cur_dir + 2) % 4)
        
    if not is_range(n_x, n_y):
        break
    else:
        cnt += 1
        cur_x, cur_y, cur_dir = n_x, n_y, n_dir


print(cnt)