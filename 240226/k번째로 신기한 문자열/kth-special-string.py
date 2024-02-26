[n, k, t] = list(input().split())

word_arr = [
    input()
    for _ in range(int(n))
]

sort_word_arr = []

for word in word_arr:
    if t == word[0:len(t)]:
        sort_word_arr.append(word)

sort_word_arr.sort()

print(sort_word_arr[int(k) - 1])