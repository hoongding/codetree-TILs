import sys
# n개 바구니, 앞 뒤 k
n, k = tuple(map(int, input().split()))

# 사탕개수, 바구니 좌표
baskets = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

max_size = -sys.maxsize
MAX_PLACE = 100

for center in range(k + 1, MAX_PLACE):
    cur_start, cur_end = center - k, center + k
    cur_sum = 0
    for candies, coor in baskets:
        if cur_start <= coor <= cur_end:
            cur_sum += candies
    max_size = max(max_size, cur_sum)

print(max_size)