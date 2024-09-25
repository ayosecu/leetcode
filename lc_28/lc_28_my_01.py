def main(haystack, needle):
    n_haystack = len(haystack)
    n_needle = len(needle)
    if n_needle > n_haystack:
        return -1
    
    i = 0
    find_idx = -1
    while i < n_haystack:
        if haystack[i] == needle[0] and n_haystack - i >= n_needle:
            find_idx = i
            for j in range(n_needle):
                if haystack[i+j] != needle[j]:
                    find_idx = -1
                    break
            if find_idx > -1:
                return find_idx
        i += 1

    return find_idx

if (__name__)==("__main__"):
    tc = [
            ["sadbutsad", "sad"],
            ["leetcode", "leeto"],
            ["sasadbcode", "sad"]
    ]

    for t in tc:
        print(main(t[0], t[1]))
