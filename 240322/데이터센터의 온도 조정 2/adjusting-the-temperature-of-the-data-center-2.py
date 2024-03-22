# 온도 a 보다 낮으면 C
# a <= tem <= b : G
# tem >= b : H

# N, C, G, H
import sys
n, c, g, h = tuple(map(int, input().split()))

temparatures = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

temparatures.sort(lambda x: x[1])

_, max_temp = temparatures[n - 1]
min_temp, _ = temparatures[0]

# G가 가장 점수 높음!! 최대한 G 많이 나오도록~
def get_work(a, b, cur):
    if cur < a:
        return c
    elif a <= cur <= b:
        return g
    else:
        return h

max_work = 0
for i in range(min_temp, max_temp + 1):
    temp_sum = 0
    for temp_a, temp_b in temparatures:
        temp_sum += get_work(temp_a, temp_b, i)
    
    max_work = max(max_work, temp_sum)


print(max_work)