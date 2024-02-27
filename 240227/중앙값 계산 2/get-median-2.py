# 중앙값? 오름차순 정렬 후 가장 중앙에 위치하는 값
n = int(input())

arr = list(map(int, input().split()))

middle_val_arr = []
for [index, num] in enumerate(arr):
    if index % 2 == 0:
        sort_arr = sorted(arr[:index + 1])
        # print(sort_arr)
        middle_val_arr.append(sort_arr[index // 2])

for num in middle_val_arr:
    print(num, end = " ")