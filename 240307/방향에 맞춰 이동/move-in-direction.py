n = int(input())

moves = [
    tuple(input().split())
    for _ in range(n)
]

# N: (0, 1) , E: (1, 0), S: (0, -1), W: (-1, 0)
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

answer = [0, 0]

for direction, distance in moves:
    distance = int(distance)
    direction_to_index = -1
    if direction == 'N':
        direction_to_index = 0
    elif direction == 'E':
        direction_to_index = 1
    elif direction == 'S':
        direction_to_index = 2
    else:
        direction_to_index = 3
    
    answer[0] += dx[direction_to_index] * distance
    answer[1] += dy[direction_to_index] * distance

print(answer[0], answer[1])