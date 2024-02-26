n = int(input())
arr = list(map(int, input().split()))

arr.sort()

sum_arr = []

for idx in range(0,len(arr)//2 + 1):
    sum_arr.append(arr[idx] + arr[len(arr) - idx - 1])

print(max(sum_arr))