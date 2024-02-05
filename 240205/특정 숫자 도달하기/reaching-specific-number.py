num_arr = map(int, input().split())

new_arr = []

for num in num_arr:
    if(num >= 250):
        break
    else:
        new_arr.append(num)

sum_num = sum(new_arr)
mean = sum_num / len(new_arr)

print(sum_num, mean)