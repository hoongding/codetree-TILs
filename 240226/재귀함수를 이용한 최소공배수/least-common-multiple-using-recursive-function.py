n = int(input())

arr = list(map(int, input().split()))

def get_GCD(a, b):
    for i in range(a if a < b else b, 0, -1):
        if a % i == 0 and b % i == 0:
            return i

def get_LCM(a, b):
    gcd = get_GCD(a, b)
    
    [aDiv, bDiv] = [a // gcd, b // gcd]

    return gcd * aDiv * bDiv

def get_answer(n):
    if n == 0:
        return arr[0]
    return get_LCM(get_answer(n - 1), arr[n - 1])

print(get_answer(n))