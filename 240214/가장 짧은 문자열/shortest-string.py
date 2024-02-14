len_arr = []

for _ in range(3):
    len_arr.append(len(input()))

print(max(len_arr) - min(len_arr))