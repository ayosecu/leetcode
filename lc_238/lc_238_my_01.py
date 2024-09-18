def main(nums):
    nums_size = len(nums)
    answer = [0]*nums_size

    zero_cnt = 0
    zero_idx = -1
    all_prod = 1

    for idx, num in enumerate(nums):
        if num != 0:
            all_prod *= num
        else:
            zero_cnt += 1
            zero_idx = idx

    if zero_cnt == 1:
        answer[zero_idx] = all_prod
    elif zero_cnt == 0:
        for idx, num in enumerate(nums):
            answer[idx] = all_prod // num

    return answer

if (__name__)==("__main__"):
    tc = [
            [1,2,3,4],
            [-1,1,0,-3,3]
            ]
    for t in tc:
        print(main(t))
    
