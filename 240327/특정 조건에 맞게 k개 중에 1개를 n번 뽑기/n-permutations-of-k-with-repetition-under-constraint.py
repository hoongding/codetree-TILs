k, n = tuple(map(int, input().split()))
answer = []

def _print():
    for num in answer:
        print(num, end=" ")
    print()

def choose(cur_num):
    if cur_num == n:
        _print()
        return
    
    for num in range(1, k + 1):
        if len(answer) >= 2:
            if answer[cur_num - 1] == num and answer[cur_num - 2] == num:
                continue
            else:
                answer.append(num)
                choose(cur_num + 1)
                answer.pop()
        else:
            answer.append(num)
            choose(cur_num + 1)
            answer.pop()


choose(0)