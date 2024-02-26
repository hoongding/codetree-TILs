[a, b, c] = list(map(int, input().split()))

prod = a * b * c

def sum_digit(n):
    if n < 10:
        return n
    
    return sum_digit(n // 10) + n % 10

print(sum_digit(prod))