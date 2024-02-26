n = int(input())

def get_answer(n):
    if n == 1: return 2
    if n == 2: return get_answer(n - 1) * 2
    
    return (get_answer(n - 1) * get_answer(n - 2)) % 100

print(get_answer(n))