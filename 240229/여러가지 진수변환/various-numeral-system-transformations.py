n, b = tuple(map(int, input().split()))


arr = []
while True:
    if n < b:
        arr.append(n)
        break
    arr.append(n % b)
    n //= b

for num in arr[::-1]:
    print(num, end="")