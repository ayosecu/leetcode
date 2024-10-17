def main(nums, val):
    match_idx = []
    unmatch_idx = []
    
    for i in range(len(nums)):
        if nums[i] == val:
            match_idx.append(i)
        else:
            unmatch_idx.append(i)
    
    unmatch_len = len(unmatch_idx)
    if unmatch_len > 0:
        ptr = len(unmatch_idx)-1
        for j in range(len(match_idx)):
            nums[match_idx[j]] = nums[unmatch_idx[ptr]]
            if ptr > 0:
                ptr -= 1
    
    return unmatch_len

if (__name__ == "__main__"):
    nums = [
                [3,2,2,3],
                [0,1,2,2,3,0,4,2]
            ]
    val = [3, 2]
    for i in range(len(nums)):
        print(main(nums[i], val[i]))
    
