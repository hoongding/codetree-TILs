import sys
n, k = list(map(int, input().split()))

# 사진크기 k
# G가 찍히면 각각 1점, H찍히면 각각 2점

# 사람위치, 알파벳정보
people = [
    input().split()
    for _ in range(n)
]

max_size = -sys.maxsize
MAX_NUM = 10000
for i in range(MAX_NUM - k + 1):

    cur_score = 0
    for idx in range(k + 1):
        for (position, alphabet) in people:
            position = int(position)
            if position == i + idx:
                if alphabet == 'G':
                    cur_score += 1
                else:
                    cur_score += 2
    max_size = max(max_size, cur_score)
    

print(max_size)