n, m = tuple(map(int, input().split()))
nums = list(map(int, input().split()))

# 음이 아닌 정수!
# 그중 m개의 숫자를 뽑아 xor 한 최대값
answer = []
max_xor = 0

def do_xor():
    
    cnt = answer[0]
    for i in range(1, m):
        cnt =  cnt ^ answer[i]
    return cnt

def choose(cur_cnt, cnt):
    global max_xor
    if cur_cnt == n:
        if cnt == m:
            max_xor = max(max_xor, do_xor())
        return
    
    answer.append(nums[cur_cnt])
    choose(cur_cnt + 1, cnt + 1)
    answer.pop()

    choose(cur_cnt + 1, cnt)
    

choose(0, 0)
print(max_xor)