n = int(input())

def get_cnt(n):
    if n == 1:
        return 0
    if n % 2 == 0:
        return get_cnt(n // 2) + 1
    else:
        return get_cnt(n // 3) + 1

print(get_cnt(n))