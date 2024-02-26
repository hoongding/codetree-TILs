n = int(input())
arr = list(map(int, input().split()))


for i in sorted(arr):
    print(i, end = " ")
print()

arr.sort(reverse=True)
for i in arr:
    print(i, end = " ")