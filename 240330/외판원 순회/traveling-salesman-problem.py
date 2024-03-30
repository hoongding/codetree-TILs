import sys
n = int(input())

weights = [
    list(map(int, input().split()))
    for _ in range(n)
]

answer = []
visited = [False for _ in range(n)]

# 다시 1번으로 돌아와야함.
def get_weights():
    temp_sum = 0
    for cur_grid, next_grid in answer:
        temp_sum += weights[cur_grid][next_grid]

    return temp_sum

min_sum = sys.maxsize
def choose(cur_num):
    global min_sum
    if len(answer) == n - 1:
        answer.append((cur_num, 0))
        min_sum = min(min_sum, get_weights())
        return
    
    for i in range(1, n):
        if visited[i]:
            continue
        
        visited[i] = True
        answer.append((cur_num, i))
        choose(i)
        answer.pop()
        visited[i] = False

visited[0] = True
choose(0)

print(min_sum)