num_arr = list(input().split())

new_arr = []

for num in num_arr:
    if(num == '0'):
        break
    new_arr.append(num)

print(" ".join(new_arr[::-1]))