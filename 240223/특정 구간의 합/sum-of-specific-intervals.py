[n, m] = map(int, input().split())
a_arr = list(map(int, input().split()))

pair_arr = [
    list(map(int, input().split()))
    for _ in range(m)
]

def find_sum(start_idx, end_idx):
    return sum(a_arr[start_idx - 1:end_idx])

def find_answer():
    _sum = []
    for [start_idx, end_idx] in pair_arr:
        _sum.append(find_sum(start_idx, end_idx))
    
    return _sum

for _sum in find_answer():
    print(_sum)