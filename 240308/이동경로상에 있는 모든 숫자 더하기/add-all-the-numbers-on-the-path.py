n, t = tuple(map(int, input().split()))
cmds = list(input())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def is_range(cur_x, cur_y):
    return cur_x >= 0 and cur_y >= 0 and cur_x < n and cur_y < n

cur_x, cur_y = (n // 2, n // 2)
cur_dir = 0
sum_val = grid[cur_x][cur_y]

def next_move(cmd):
    global cur_dir
    global cur_x
    global cur_y
    global sum_val

    if cmd == 'R':
        cur_dir = (cur_dir + 1) % 4
    elif cmd == 'L':
        cur_dir = (cur_dir + 3) % 4
    # F일때 앞으로 한칸!
    else:
        n_x, n_y = cur_x + dirs[cur_dir][0], cur_y + dirs[cur_dir][1]    

        if is_range(n_x, n_y):
            sum_val += grid[n_x][n_y]
            cur_x = n_x
            cur_y = n_y
    

for cmd in cmds:
    next_move(cmd)

print(sum_val)