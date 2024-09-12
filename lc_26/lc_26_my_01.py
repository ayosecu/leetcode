def main(nums):
    size_nums = len(nums)
    if size_nums <= 1:
        return size_nums
    
    ptr = 0
    nxt = 1
    cnt = 1
    while nxt < size_nums:
        if nums[nxt] != nums[ptr]:
            ptr += 1
            nums[ptr] = nums[nxt]
            cnt += 1
        nxt += 1
    return cnt

if (__name__ == "__main__"):
    nums = [
                [1,1,2],
                [0,0,1,1,1,2,2,3,3,4]
            ]
    for i in range(len(nums)):
        print(main(nums[i]))
    
