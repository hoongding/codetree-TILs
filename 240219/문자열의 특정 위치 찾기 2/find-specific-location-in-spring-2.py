strings = ['apple', 'banana', 'grape', 'blueberry', 'orange']
alphabet = input()

cnt = 0
sort_strings = []

for string in strings:
    if(string[2] == alphabet or string[3] == alphabet):
        cnt += 1
        sort_strings.append(string)

for string in sort_strings:
    print(string)
print(cnt)