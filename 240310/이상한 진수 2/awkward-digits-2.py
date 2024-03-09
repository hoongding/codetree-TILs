import sys
two_digit = list(map(int, list(input())))
two_digit.reverse()

#
max_val = -sys.maxsize
for i in range(len(two_digit)):
    cur_val = 0
    for (index, digit) in enumerate(two_digit):
        if i == index:
            new_digit = 0 if digit == 1 else 1
            cur_val += new_digit * (2 ** index)
        else:
            cur_val += digit * (2 ** index)
    
    max_val = max(max_val, cur_val)

print(max_val)