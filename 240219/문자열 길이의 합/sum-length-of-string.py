n = int(input())

arr = [
    input()
    for _ in range(n)
]

target = 'a'

cnt = 0
length = 0

for string in arr:
    length = length + len(string)
    if(string[0] == 'a'):
        cnt += 1

print(length, cnt)