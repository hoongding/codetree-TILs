n = int(input())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [False for _ in range(n)]
answer = []

def get_sum():
    temp_sum = 0
    for idx, num in enumerate(answer):
        temp_sum += grid[idx][num]
    
    return temp_sum
max_sum = 0
def choose(cur_num):
    global max_sum
    if cur_num == n:
        max_sum = max(max_sum, get_sum())
        return
    
    for i in range(n):
        if visited[i]:
            continue
        visited[i] = True
        answer.append(i)
        choose(cur_num + 1)
        answer.pop()
        visited[i] = False

choose(0)

print(max_sum)