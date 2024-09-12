def main(nums1, nums2, m, n):
        result = [0] * (m+n)
        i = 0
        j = 0
        k = 0

        if m == 0:
            for num in nums2:
                nums1[i] = num
                i += 1
            return
        if n == 0:
            return
        
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                result[k] = nums1[i]
                i += 1
            else:
                result[k] = nums2[j]
                j += 1
            k += 1
        while i < m:
            result[k] = nums1[i]
            i += 1
            k += 1
        while j < n:
            result[k] = nums2[j]
            j += 1
            k += 1
        
        i = 0
        while i < m + n:
            nums1[i] = result[i]
            i += 1

if (__name__ == "__main__"):
    nums1 = [
                [1,2,3,0,0,0],
                [1],
                [0]
            ]
    nums2 = [
                [2,5,6],
                [],
                [1]

            ]
    m = [3, 1, 0]
    n = [3, 0, 1]

    for i in range(len(nums1)):
        main(nums1[i], nums2[i], m[i], n[i])
        print(nums1[i])
    
