[a, b] = map(int, input().split())



def convert_num (a, b):
    [small_num, big_num] = [min(a, b), max(a, b)]

    change = False
    if small_num != a:
        change = True
    
    return [small_num + 10, big_num * 2] if not change else [big_num * 2, small_num + 10]


[convert_a, convert_b] = convert_num(a, b)

print(convert_a, convert_b)