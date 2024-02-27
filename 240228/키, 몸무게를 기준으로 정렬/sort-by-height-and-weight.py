n = int(input())

# 키 기준 오름차순 > 몸무게 더 큰사람
people = [
    tuple(input().split())
    for _ in range(n)
]

people.sort(key=lambda person:(int(person[1]), -int(person[2])))

for person in people:
    name, height, weight = person
    print(name, height, weight)