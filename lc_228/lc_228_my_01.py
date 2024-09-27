def main(nums):
    result = []

    range_cnt = 0
    prv_num = 0
    for num in nums:
        if range_cnt == 0:
            result.append([str(num)])
            range_cnt += 1
        elif num == prv_num + 1:
            if len(result[range_cnt-1]) > 1:
                result[range_cnt-1][1] = str(num)
            else:    
                result[range_cnt-1].append(str(num))
        else:
            result.append([str(num)])
            range_cnt += 1
        prv_num = num

    for i in range(range_cnt):
        result[i] = "->".join(result[i])

    return result

if (__name__)==("__main__"):
    tc = [
            [0,1,2,4,5,7],
            [0,2,3,4,6,8,9]
    ]

    for t in tc:
        print(main(t))