n, k = tuple(map(int, input().split()))

arr = [
    tuple(map(int, input().split()))
    for _ in range(k)
]

target_arr = [ 0 for _ in range(n)]

def stack_block(start, end):
    for idx in range(start - 1, end):
        target_arr[idx] += 1

for cmd in arr:
    start, end = cmd
    stack_block(start, end)

print(max(target_arr))