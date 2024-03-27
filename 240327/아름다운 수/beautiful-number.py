# 1 ~ 4 이하의 숫자로 이루어진 숫자
n = int(input())
nums = [1, 2, 3, 4]
answer = []
cnt = 0

def choose(cur_len):
    global cnt
    if len(answer) == n:
        cnt += 1
        return
    
    for target_num in nums:
        if cur_len + target_num <= n:
            for i in range(target_num):
                answer.append(target_num)
            choose(cur_len + target_num)
            for i in range(target_num):
                answer.pop()
    

choose(0)
print(cnt)