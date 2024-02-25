n = int(input())

def recursive_print(num):
    if num == 0: return

    print(num, end=" ")
    recursive_print(num - 1)
    print(num, end=" ")
    
recursive_print(n)