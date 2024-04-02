import sys
MAX_SIZE = sys.maxsize
n = int(input())

grid = [
    list(input())
    for _ in range(n)
]

# 시작점에서 출발 -> 최소 3개의 동전 수집 -> 도착점
# 단, 동전은 번호가 증가하는 순서대로 수집
# 해당 위치를 지나가도, 동전을 수집하지 않아도 됨.
# 같은 위치를 2번 이상 지나는 것 허용
# 불가능 하다면 -1을 출력
start_pos, end_pos = (-1, -1), (-1, -1)
selected_pos = []
coin_pos = []
answer = MAX_SIZE

# 3. 이동하는 거리 구하는 함수
def dist(a, b):
    (ax, ay), (bx, by) = a, b
    return abs(ax - bx) + abs(ay - by)

def calc():
    num_moves = dist(start_pos, selected_pos[0])
    for i in range(2):
        num_moves += dist(selected_pos[i], selected_pos[i + 1])
    num_moves += dist(selected_pos[2], end_pos)

    return num_moves


# find 함수 작성
def find(cur_coin, coin_cnt):
    global answer

    if coin_cnt == 3:
        answer = min(answer, calc())
        return
    
    # 동전 개수만큼 다 넣었을 경우 그냥 return
    if cur_coin == len(coin_pos):
        return

    # 동전 선택하지 않을 때.    
    find(cur_coin + 1, coin_cnt)

    # 현재 동전 선택할 경우.
    selected_pos.append(coin_pos[cur_coin])
    find(cur_coin + 1, coin_cnt + 1)
    selected_pos.pop()


# 1. start, end position부터 잡아준다. -> O(n^2)
for i in range(n):
    for j in range(n):
        if grid[i][j] == 'S':
            start_pos = (i, j)
        if grid[i][j] == 'E':
            end_pos = (i, j)

# 2. 동전 위치 찾기 1 ~ 9까지
for num in range(1, 10):
    for i in range(n):
        for j in range(n):
            if grid[i][j] == str(num):
                coin_pos.append((i, j))

find(0, 0)

if answer == MAX_SIZE:
    print(-1)
else:
    print(answer)