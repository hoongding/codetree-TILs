# n번의 턴에 숫자가 주어지고, 각 턴마다 하나의 말을 선택해서 해당 숫자만큼 앞으로 나아가기
# 숫자 m 번에 도달하면, 1점 얻기
# n번의 턴에 대해 움직일 말을 적절하게 선택해서, 얻을 수 있는 최대 점수
# n: 턴수, m: 윷놀이 판, k: 말의수
n, board_num, player_num = tuple(map(int, input().split()))

# player 숫자만큼 board 만들어주기
moves = list(map(int, input().split()))
players = [1 for _ in range(player_num)]
# 시작은 1부터 시작. board_num 까지 도착하면 끝.
max_cnt = 0

def calc():
    score = 0
    for player in players:
        score += (player >= board_num)

    return score

def choose_move(cnt):
    # 보드 크기보다 높으면
    global max_cnt

    max_cnt = max(max_cnt, calc())
    if cnt == n:
        return
    
    for i in range(player_num):
        if players[i] >= board_num:
            continue
        
        players[i] += moves[cnt]
        choose_move(cnt + 1)
        players[i] -= moves[cnt]
        

choose_move(0)
print(max_cnt)