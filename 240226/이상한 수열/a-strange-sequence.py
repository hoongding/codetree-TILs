n = int(input())

def get_answer(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    return get_answer(n // 3) + get_answer(n - 1)

print(get_answer(n))