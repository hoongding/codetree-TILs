row, col = tuple(map(int, input().split()))

answer = [
    [0] * row
    for _ in range(col)
]

# [col][row]
# 동(0, 1) 남(1, 0) 서(0, -1) 북(-1, 0)
dcol, drow = [0, 1, 0, -1], [1, 0, -1, 0]

def is_range(cur_col, cur_row):
    return cur_col >= 0 and cur_row >= 0 and cur_col < col and cur_row < row

dir_idx = 0
cur_col, cur_row = 0, 0

answer[cur_col][cur_row] = 1
for cur_num in range(2, row * col + 1):
    n_col, n_row = cur_col + dcol[dir_idx], cur_row + drow[dir_idx]
    
    # range를 넘어가면 dir_idx를 하나 더해준다.
    if not is_range(n_col, n_row) or answer[n_col][n_row] != 0:
        dir_idx = (dir_idx + 1) % 4
        
    cur_col, cur_row = cur_col + dcol[dir_idx], cur_row + drow[dir_idx]
    answer[cur_col][cur_row] = cur_num

for row in answer:
    for box in row:
        print(box, end=" ")
    
    print()