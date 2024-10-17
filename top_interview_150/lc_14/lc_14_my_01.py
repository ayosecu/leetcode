def main(strs):

    v = sorted(strs)
    print(v)
    print("min : ", min(len(v[0]), len(v[-1])))
    ret = ""
    n_strs = len(strs)
    min_str_n = 200
    for s in strs:
        s_n = len(s)
        if s_n < min_str_n:
            min_str_n = s_n

    i = 0
    while i < min_str_n:
        ch = strs[0][i]
        j = 1
        cnt = 1
        while j < n_strs:
            if strs[j][i] == ch:
                cnt += 1
            else:
                return ret
            j += 1
        if cnt == n_strs:
            ret += ch
        i += 1
    return ret

if (__name__)==("__main__"):
    tc = [
            ["flower","flow","flight"],
            ["dog","racecar","car"]
        ]
    
    for t in tc:
        print(main(t))
