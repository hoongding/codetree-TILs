brackets = list(input())

cnt = 0
for i in range(len(brackets)):
    for j in range(i + 1, len(brackets) - 1):
        if brackets[i] == '(' and brackets[i + 1] == '(' and brackets[j] == ')' and brackets[j + 1] == ')':
                cnt += 1

print(cnt)