import sys

n = int(input())
min_val = sys.maxsize
people = list(map(int, input().split()))

for i in range(n):
    cur_sum = 0
    for j in range(n):
        if i != j:
            difference = abs(i - j)
            cur_sum += difference * people[j]
    
    min_val = min(min_val, cur_sum)

print(min_val)