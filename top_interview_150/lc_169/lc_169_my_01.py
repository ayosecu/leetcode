def main(nums):
    dic = {}
    size_nums = len(nums)
    max_num = 0
    for num in nums:
        if num in dic:
            dic[num] += 1
        else:
            dic[num] = 1

    for num, count in dic.items():
        if count > size_nums / 2:
            return num

    return 0

if (__name__ == "__main__"):
    nums = [
                [3,2,3],
                [2,2,1,1,1,2,2]
            ]
    for i in range(len(nums)):
        print(main(nums[i]))
    
