n = int(input())

nums = [
    int(input())
    for _ in range(n)
]

print(nums)

for (index, num) in enumerate(nums):
    print(index)