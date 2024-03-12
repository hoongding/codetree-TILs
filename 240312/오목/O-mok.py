# 연속 가로 + 1   row + 1
# 연속 세로 + 1   col + 1
# 오른쪽 대각선 row, col 각각 + 1
# 왼쪽 대각선 row, col 각각 -1
import sys
grid = [
    list(map(int, input().split()))
    for _ in range(19)
]

dxs, dys = [1, 1, 1, -1, -1, -1, 0, 0], [-1, 0, 1, -1, 0, 1, -1, 1]

def is_range(row, col):
    return row >= 0 and col >= 0 and row < len(grid) and col < len(grid)

# 연속 가로 check
for i in range(len(grid)):
    for j in range(len(grid)):
        if grid[i][j] == 0:
            continue
        
        for dx, dy in zip(dxs, dys):
            curt = 1
            curx = i
            cury = j
            while True:
                nx = curx + dx
                ny = cury + dy
                if is_range(nx, ny) == False:
                    break
                if grid[nx][ny] != grid[i][j]:
                    break
                curt += 1
                curx = nx
                cury = ny
            
            if curt == 5:
                print(grid[i][j])
                print(i + 2 * dx + 1, j + 2 * dy + 1)
                sys.exit()

print(0)