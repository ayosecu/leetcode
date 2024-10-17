def main(nums):
    nums_size = len(nums)

    if nums_size == 1:
        return True

    last_idx = nums_size - 1
    ladder = [0] * 10000
    for i in range(nums_size-1):
        if last_idx - i <= nums[i]:
            return True
        else:
            for j in range(nums[i]):
                ladder[i+j] += 1
            if ladder[i] == 0:
                return False

    return False

if (__name__ == "__main__"):
    tc = [
            [2, 3, 1, 1, 4],
            [3, 2, 1, 0, 4],
            [1, 2],
            [2, 4, 1],
            [1],
            [0, 2, 3],
            [1,0,1,0]
         ]
    
    for t in tc:
        print(main(t))
    
