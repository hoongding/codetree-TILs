n = int(input())

# 1이상 n*n 이하의 숫자, 중복없이 단 한번만
# 여덟방향 중 한 방향

grid_info = [
    list(map(int, input().split()))
    for _ in range(n)
]

grid_direction = [
    list(map(int, input().split()))
    for _ in range(n)
]

s_row, s_col = tuple(map(int, input().split()))

# 특정 위치에서 시작해서, 현재 위치에 적혀있는 방향에 있는 숫자들 중, 현재 숫자보다 더 큰 숫자가 적혀있는 곳으로
# 이동하고 싶음

directions = [
    [0, 0],
    [-1, 0],
    [-1, 1],
    [0, 1],
    [1, 1],
    [1, 0],
    [1, -1],
    [0, -1],
    [-1, -1],
]

# 방향에 놓여있는 모든 곳을 갈 수 있음. 단, 현재 숫자보다 높은 곳으로

def is_range(x, y):
    return x >= 0 and y >= 0 and x < n and y < n

answer = 0
def move(x, y, move_cnt):
    global answer
    # 현재 격자에 쓰여있는 num
    target_num = grid_info[x][y]
    # 현재 격자의 direction
    dx, dy = directions[grid_direction[x][y]]
    # 한번 이동 성공할때마다 answer max 해주기
    answer = max(answer, move_cnt)
    temp_x, temp_y = x + dx, y + dy
    temp_coors = []
    # 이동 가능한 좌표 배열을 구해준다.
    while(is_range(temp_x, temp_y)):
        temp_coors.append((temp_x, temp_y))
        temp_x += dx
        temp_y += dy
    
    # 이동가능한 좌표가 없을경우 return
    if len(temp_coors) == 0:
        return
    # 이동가능한 좌표 중, 나보다 큰 놈이 없을경우 return
    available_coors = []
    for c_x, c_y in temp_coors:
        if grid_info[c_x][c_y] > target_num:
            available_coors.append((c_x, c_y))
    else:
        if len(available_coors) == 0:
            return
    
    for a_x, a_y in available_coors:
        move(a_x, a_y, move_cnt + 1)

move(s_row - 1, s_col - 1, 0)

print(answer)