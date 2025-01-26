def main(nums):
    size_nums = len(nums)
    wp = 0
    p = 1
    counter = 1
    while p < size_nums:
        if nums[p] == nums[wp]:
            if counter == 1:
                wp += 1
                nums[wp] = nums[p]
                counter += 1
            else:
                if p == size_nums - 1:
                    return wp + 1                    
                wp += 1
                while nums[p+1] == nums[p]:
                    if p + 1 == size_nums - 1:
                        return wp
                    p += 1
                p += 1
                nums[wp] = nums[p]
                counter = 1
        else:
            wp += 1
            nums[wp] = nums[p]
            counter = 1
        p += 1
    return wp+1

if (__name__ == "__main__"):
    nums = [
                [1,1,1,2,2,3],
                [0,0,1,1,1,1,2,3,3]
            ]
    for i in range(len(nums)):
        print(main(nums[i]))
    
