_string = list(input())
target = input()

def is_substring():
    for [index, _str] in enumerate(_string[:len(_string) - (len(target) - 1)]):
        if "".join(_string[index: index + len(target)]) == target:
            return index

    return -1
        
print(is_substring())