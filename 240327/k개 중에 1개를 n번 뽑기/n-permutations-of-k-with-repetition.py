k, n = tuple(map(int, input().split()))

# 1~k 까지 숫자. n 번 반복

answer = []
def _print():
    for char in answer:
        print(char, end = " ")
    print()

def choose(cur_num):
    if cur_num == n:
        _print()
        return
    
    for num in range(1, k + 1):
        answer.append(num)
        choose(cur_num + 1)
        answer.pop()

choose(0)