n = int(input())

def get_answer(n):
    if n == 1:
        return 0
    
    if n % 2 == 0:
        return get_answer(n // 2) + 1
    if n % 2 == 1:
        return get_answer(n * 3 + 1) + 1

print(get_answer(n))