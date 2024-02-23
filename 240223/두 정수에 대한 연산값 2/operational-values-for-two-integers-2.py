[a, b] = map(int, input().split())

[small_num, big_num] = [min(a, b), max(a, b)]

print(small_num + 10, big_num * 2)