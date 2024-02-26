n = int(input())

a_arr = list(map(int, input().split()))
b_arr = list(map(int, input().split()))

a_arr.sort()
b_arr.sort()

def get_answer(a_arr, b_arr):
    for [index, num] in enumerate(a_arr):
        if b_arr[index] != num:
            return 'No'
    
    return 'Yes'

print(get_answer(a_arr, b_arr))