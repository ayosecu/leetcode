def main(nums, k):
    size_nums = len(nums)
    k = k % size_nums

    if k != 0:
        nums[k:], nums[:k] = nums[:-k], nums[-k:]

    return

if (__name__ == "__main__"):
    tc = [
            [1,2,3,4,5,6,7],
            [-1,-100,3,99]
         ]
    k = [3, 2]
    for i in range(len(tc)):
        main(tc[i], k[i])
        print(tc[i])
    
