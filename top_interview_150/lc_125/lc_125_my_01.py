def main(s):
    ts = s.strip().lower()

    n = len(ts)
    if n <= 1:
        return True
    
    lp, rp = 0, n-1
    while lp < rp:
        if ts[lp].isalnum() == False:
            lp += 1
            continue
        if ts[rp].isalnum() == False:
            rp -= 1
            continue
        if ts[lp] == ts[rp]:
            lp += 1
            rp -= 1
        else:
            return False
        
    return True

if (__name__)==("__main__"):
    tc = [
            "A man, a plan, a canal: Panama",
            "race a car",
            " ",
            "0P"
    ]

    for t in tc:
        print(main(t))
