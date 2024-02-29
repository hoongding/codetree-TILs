a, b = tuple(map(int, input().split()))
n = list(map(int, list(input())))

ten_num = 0

for index, digit in enumerate(n[::-1]):
    ten_num += a ** index * digit 


answer_arr = []
while True:
    if ten_num < b:
        answer_arr.append(ten_num)
        break
    answer_arr.append(ten_num % b)
    ten_num //= b

for num in answer_arr[::-1]:
    print(num, end="")