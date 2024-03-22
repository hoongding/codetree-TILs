import sys
x, y = tuple(map(int, input().split()))

# x <= num <= y : 이 숫자들 중에 각 자리 숫자의 합이 최대가 되도록 하는
max_sum = -sys.maxsize

for num in range(x, y + 1):
    digits = list(map(int, list(str(num))))
    temp_sum = sum(digits)

    max_sum = max(max_sum, temp_sum)

print(max_sum)