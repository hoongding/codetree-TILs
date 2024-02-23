[n, m] = map(int, input().split())
a_arr = map(int, input().split())

pair_arr = [
    list(map(int, input().split()))
    for _ in range(m)
]

print(pair_arr)

def find_sum(start_idx, end_idx):
    print(start_idx)
    return sum(a_arr[start_idx:end_idx])

def find_answer():
    _sum = []
    for [start_idx, end_idx] in pair_arr:
        _sum.append(find_sum(start_idx, end_idx))
    
    return _sum

print(find_answer())