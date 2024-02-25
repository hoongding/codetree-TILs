n = int(input())

def _print(n):
    if n == 0: return
    _print(n - 1)
    print(n, end = " ")

def _print_2(n):
    if n == 0: return
    print(n, end = " ")
    _print_2(n - 1)

_print(n)
print()
_print_2(n)