n = list(map(int, list(input())))

ten_n = 0
for index, num in enumerate(n[::-1]):
    ten_n += (2 ** index) * num

ten_n *= 17

arr = []

while True:
    if ten_n < 2:
        arr.append(ten_n)
        break
    arr.append(ten_n % 2)
    ten_n //= 2

for num in arr[::-1]:
    print(num, end="")