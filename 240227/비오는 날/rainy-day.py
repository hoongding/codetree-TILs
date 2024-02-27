n = int(input())

data = [
    tuple(input().split())
    for _ in range(n)
]

rainy_data = []

for index in range(n):
    _, _, weather = data[index]
    if weather == 'Rain':
        rainy_data.append(data[index])

min_idx = 0
if len(rainy_data) == 1:
    date, day, weather = rainy_data[0]
    print(f'{date} {day} {weather}')
else:
    for i in range(1, len(rainy_data)):
        a_date, _, _ = rainy_data[min_idx]
        b_date, _, _ = rainy_data[i]
        if a_date > b_date:
            min_idx = i
    date, day, weather = rainy_data[min_idx]
    print(f'{date} {day} {weather}')