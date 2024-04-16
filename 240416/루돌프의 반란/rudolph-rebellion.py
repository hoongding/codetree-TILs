# 루돌프 move -> 1번 ~ P번 산타까지 순서대로 움직
# 기절해 있는 산타, 격자 밖 산타 못움직임

# 루돌프 -> 가장 가까운 산타향해 1칸 돌진(탈락 안한 산타 중 가장 가까운 산타)
# 가까운 산타 2명 이상이면 r 좌표가 큰 산타를 향해 돌진 r > c
# 8방향 중 하나로 돌진 가능

# 산타
# 1 ~ P 
# 산타 루돌프에게 거리가 가장 가까워지는 방향 1칸 움직
# 산타는 상하좌우 밖에 못감.
# 움직일 수 있는 칸 없으면 안감
# 루돌프로부터 가까워질 수 있는 방법 없으면 안움직임

# 충돌
# 루돌프가 움직여서 충돌 -> 산타 C만큼의 점수를 얻음, 산타는 루돌프가 이동해온 방향으로 C칸 방향으로 밀려남
# 산타가 움직여서 충돌 => D민큼의 점수 얻고, 자신이 이동해온 반대방향으로 D칸 밀려남
# 게임판 밖으로 밀려나면, 산타는 게임에서 탈락
# 밀려난 칸에 다른 산타 있으면 상호작용

# 상호작용
# 산타는 충돌 후 착지하게 되는 칸에 다른 산타가 있다면, 다른 산타는 1칸 해당 방향으로 밀려남
# 그 옆에 산타가 있다면, 연쇄적으로 1칸씩 밀려나는것을 반복.
# 게임판 밖으로 밀려나온 산타는 게임 탈락

# 기절
# 루돌프와 충돌 후 기절
# k턴이면 k + 1 까지 기절, k + 2때 다시 정상
# 루돌프 기절 산타 돌진대상 ok

# 산타 탈락 안했으면 1점씩.
# 각 산타가 얻은 최종 점수 순서대로 출력

class Santa:
    def __init__(self, num, row, col):
        self.num = num
        self.row = row
        self.col = col
        # 기절은 k턴 -> k + 2때부터 움직일 수 있음.
        self.is_faint = -1
        self.score = 0

    def rudolph_collision(self, direction):
        dx , dy = direction
        dx = dx * r_power
        dy = dy * r_power

        
        self.row += dx
        self.col += dy

        is_range(self.row, self.col)

    def santa_collision(self, direction):
        dx, dy = direction
        dx = dx * s_power
        dy = dy * s_power

        self.row += dx
        self.col += dy

        is_range(self.row, self.col)


n, turn, santa_num, r_power, s_power = tuple(map(int, input().split()))
r_row, r_col = tuple(map(int, input().split()))

santas = []

# 상하좌우
santa_move = [
    (-1, 0), (0, 1), (1, 0), (0, -1)
]
# 대각선까지 ok
rudolph_move = [
    (1, 0), (0, 1), (-1, 0), (0, -1), (1, -1), (-1, -1), (1, 1), (-1, 1)
]

for _ in range(santa_num):
    num, row, col = tuple(map(int, input().split()))
    santas.append(Santa(num, row, col))

# 산타 탈락 유무 확인
def is_range(row, col):
    return row >= 0 and col >= 0 and row < n and row < n

def calc(a, b):
    a_row, a_col = a
    b_row, b_col = b

    return (a_row - b_row) ** 2 + (a_col - b_col) ** 2

def is_exit():
    temp_exit = True
    for santa in santas:
        santa_exit = is_range(santa.row, sata.col)
        if not santa_exit:
            temp_exit = False
            break
    
    return temp_exit

def find_target_santa():

    candidate = []
    for santa in santas:
        # 게임 아웃된 산타 빼고 진행.
        if is_range(santa.row, santa.col):


# 게임 턴수만큼 게임 진행
for cur_turn in range(1, turn + 1):