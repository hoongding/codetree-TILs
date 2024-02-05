n = int(input())
subject_scores = list(map(float, input().split()))

mean = sum(subject_scores) / n

print(f"{mean:.1f}")
if mean >= 4.0:
    print('Perfect')
elif mean >= 3.0:
    print('Good')
else:
    print('Poor')