# x <= num <= y : 흥미로운 숫자 세기
# 모든 자릿수에 있는 숫자들이 같지만, 정확히 하나만 다른 숫자
# 33335, 1118 : 흥미로운 숫자!
from collections import Counter
x, y = tuple(map(int, input().split()))

cnt = 0
for num in range(x, y + 1):
    digits = Counter(map(int, list(str(num))))

    if len(digits) != 2:
        continue

    _, least_cnt = digits.most_common()[-1]
    if least_cnt != 1:
        continue
    cnt += 1

print(cnt)