n = int(input())

def print_str(n):
    if n == 0:
        return
    
    print('* ' * n)
    print_str(n - 1)
    print('* '* n)

print_str(n)