blocks = [
    [
        [1, 1, 1],
        [0, 0, 0],
        [0, 0, 0]
    ],
    [
        [1, 0, 0],
        [1, 0, 0],
        [1, 0, 0]
    ],
    [
        [1, 0, 0],
        [1, 1, 0],
        [0, 0, 0]
    ],
    [
        [0, 1, 0],
        [1, 1, 0],
        [0, 0, 0]
    ],
    [
        [1, 1, 0],
        [1, 0, 0],
        [0, 0, 0]
    ],
    [
        [1, 1, 0],
        [0, 1, 0],
        [0, 0, 0]
    ],
]

n, m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]


def max_sum(x, y):
    max_sum = 0
    for i in range(len(blocks)):
        is_possible = True
        sum_of_nums = 0
        for dx in range(0, 3):
            for dy in range(0, 3):
                if blocks[i][dx][dy] == 0:
                    continue
                if x + dx >= n or y + dy >= m:
                    is_possible = False
                else:
                    sum_of_nums += grid[x + dx][y + dy]
            
        if is_possible:
            max_sum = max(max_sum, sum_of_nums)
        

    return max_sum

answer = 0

for i in range(n):
    for j in range(m):
        answer = max(answer, max_sum(i, j))

    

print(answer)