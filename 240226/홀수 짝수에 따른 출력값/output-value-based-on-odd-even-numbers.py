n = int(input())

def get_sum_odd(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return get_sum_odd(n - 1)
    else:
        return get_sum_odd(n - 1) + n

def get_sum_even(n):
    if n == 2:
        return 2
    if n % 2 == 1:
        return get_sum_even(n - 1)
    else:
        return get_sum_even(n - 1) + n

print(get_sum_odd(n) if n % 2 == 1 else get_sum_even(n))