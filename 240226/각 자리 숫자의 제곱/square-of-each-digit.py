n = int(input())

def get_answer(n):
    if n < 10: return n**2

    return get_answer(n // 10) + (n % 10)**2


print(get_answer(n))