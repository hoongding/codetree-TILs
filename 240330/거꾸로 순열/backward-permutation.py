n = int(input())

visited = [False for _ in range(n)]
answer = []

def _print():
    for string in answer:
        print(string, end = " ")
    print()


def choose(cur_num):
    if cur_num == n + 1:
        _print()
        return
    
    for i in range(n, 0, -1):
        if visited[i - 1]:
            continue
        visited[i - 1] = True
        answer.append(i)
        choose(cur_num + 1)
        answer.pop()
        visited[i - 1] = False


choose(1)