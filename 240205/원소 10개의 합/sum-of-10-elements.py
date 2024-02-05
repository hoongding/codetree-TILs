from functools import reduce

arr = list(map(int, input().split(' ')))

print(reduce(lambda acc, num: acc + num, arr, 0))