import sys
n = int(input())

nums = [
    int(input())
    for _ in range(n)
]

def is_carry(n1, n2, n3):
    flag = False
    while n1 > 1 and n2 > 1 and n3 > 1:
        n1_digit, n2_digit, n3_digit = n1 % 10, n2 % 10, n3 % 10
        if n1_digit + n2_digit + n3_digit >= 10:
            flag = True
        
        n1 //= 10
        n2 //= 10
        n3 //= 10
    
    return flag
        

    
max_sum = -1
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if not is_carry(nums[i], nums[j], nums[k]):
                max_sum = max(max_sum, nums[i] + nums[j] + nums[k])


print(max_sum)