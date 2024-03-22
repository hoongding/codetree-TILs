x, y = tuple(map(int, input().split()))

cnt = 0
for num in range(x, y + 1):
    digit = list(str(num))
    reverse_digit = list(reversed(digit))

    if digit == reverse_digit:
        cnt += 1

print(cnt)