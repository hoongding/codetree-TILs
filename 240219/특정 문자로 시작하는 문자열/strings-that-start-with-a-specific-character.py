n = int(input())

arr = [
    input()
    for _ in range(n)
]

target = input()
cnt = 0
length = 0

for string in arr:
    if(string[0] == target):
        cnt += 1
        length += len(string)

print(cnt, f"{length / cnt:.2f}")