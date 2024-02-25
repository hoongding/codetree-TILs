n = int(input())

def _sum(num):
    if num == 0: return 0

    return _sum(num - 1) + num

print(_sum(n))