n = int(input())

numbers = list(map(int, input().split()))

even_numbers = []

for number in numbers:
    if(number % 2 == 0):
        even_numbers.append(number)

print(" ".join(map(str, even_numbers[::-1])))