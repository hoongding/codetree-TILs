import sys
n, h, t = tuple(map(int, input().split()))

heights = list(map(int, input().split()))

# 최소 t번 이상 h 높이만큼 맞추고 싶다. 어떻게 하면 좋을까?
min_cost = sys.maxsize
for i in range(n - t + 1):
    costs = 0
    for idx in range(i, i + t):
        costs += abs(h - heights[idx])
    
    min_cost = min(min_cost, costs)

print(min_cost)