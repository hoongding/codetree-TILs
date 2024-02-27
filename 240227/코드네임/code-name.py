class Person:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def _print(self):
        print(f'{self.name} {self.score}')


arr = [
    tuple(input().split())
    for _ in range(5)
]

object_arr = []

for i in range(5):
    name, score = arr[i]
    score = int(score)

    object_arr.append(Person(name, score))

min_idx = 0
for i in range(1, 5):
    if object_arr[min_idx].score > object_arr[i].score:
        min_idx = i

object_arr[min_idx]._print()