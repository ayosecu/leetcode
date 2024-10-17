def main(nums):
    nums_size = len(nums)

    if nums_size == 1:
        return 0

    last_idx = nums_size - 1
    step = 0
    i = 0
    while i < nums_size-1:
        if last_idx - i <= nums[i]:
            return step + 1

        jump_range = 0
        jump_idx = 0
        for j in range(1, nums[i]+1):
            if i+j+nums[i+j] > jump_range:
                jump_range = i+j+nums[i+j]
                jump_idx = i+j
        i = jump_idx
        step += 1                 
        
    return step

if (__name__ == "__main__"):
    tc = [
            [2, 3, 1, 1, 4],
            [2, 3, 0, 1, 4],            
            [1, 2],
            [2, 4, 1],
            [1],
            [1,2,1,1,1],
            [1,1,1,1]
         ]
    
    for t in tc:
        print(main(t))
    
