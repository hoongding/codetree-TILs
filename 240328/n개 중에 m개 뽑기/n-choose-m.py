# combination 구하기
n, m = tuple(map(int, input().split()))
# num 중 안겹치게 m개 뽑기
nums = [i for i in range(1, n + 1)]
answer = []

def _print():
    for string in answer:
        print(string, end=" ")
    print()

def choose(cur_cnt, cnt):
    if cur_cnt == n + 1:
        if cnt == m:
            _print()        
        return
    
    answer.append(cur_cnt)
    choose(cur_cnt + 1, cnt + 1)
    answer.pop()

    choose(cur_cnt + 1, cnt)

choose(1, 0)