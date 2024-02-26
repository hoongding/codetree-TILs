n = int(input())

arr = [
    input()
    for _ in range(n)
]

arr.sort()

for word in arr:
    print(word)