n, m = list(map(int, input().split()))

grid = [
    list(input().split())
    for _ in range(n)
]

# W 하얀색 B 검은색
# 이동은 점프만? 점프진행시, 현재 위치 색 != 점프한 칸 색
# 현재 위치에서 적어도 한칸 이상 오른쪽 위치 or 아래쪽 한칸 이상
# row + 1, col + 1

cnt = 0
for i in range(1, n):
    for j in range(1, m):
        for k in range(i + 1, n - 1):
            for l in range(j + 1, m - 1):
                if grid[0][0] != grid[i][j] and \
                   grid[i][j] != grid[k][l] and \
                   grid[k][l] != grid[n - 1][m - 1]:
                    cnt += 1

print(cnt)