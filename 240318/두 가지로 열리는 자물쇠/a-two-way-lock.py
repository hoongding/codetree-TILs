# 1 ~ N 이 인접한 원형 자물쇠
# 첫번쨰 조합과 거리가 2 이내, 모든 자리에 대해 두번쨰 조합과 거리가 2이내에 있으면 열린다 

n = int(input())

first = list(map(int, input().split()))
second = list(map(int, input().split()))


def is_range(num, digit):
    first_digit, second_digit = first[digit], second[digit]
    first_match = False
    second_match = False
    
    for idx in range(-2, 3):
        temp_num = num + idx
        
        if temp_num <= 0:
            temp_num = n + temp_num - 1
        if temp_num > n:
            temp_num = temp_num - n
        
        if temp_num == first_digit: first_match = True
        if temp_num == second_digit: second_match = True
    
    return (first_match, second_match)


cnt = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            f_first_match, f_second_match = is_range(i, 0)
            s_first_match, s_second_match = is_range(j, 1)
            t_first_match, t_second_match = is_range(k, 2)

            first_match = f_first_match and s_first_match and t_first_match
            second_match = f_second_match and s_second_match and t_second_match
        
            if first_match or second_match:
                cnt += 1
    
print(cnt)