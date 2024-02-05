scores = list(map(float, input().split()))

avg = sum(scores) / len(scores)

print(f"{avg:.1f}")