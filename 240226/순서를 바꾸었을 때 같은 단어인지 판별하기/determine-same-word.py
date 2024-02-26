arr = [
    input()
    for _ in range(2)
]

a_string = list(arr[0])
b_string = list(arr[1])

a_string.sort()
b_string.sort()

print('Yes' if "".join(a_string) == "".join(b_string) else 'No')