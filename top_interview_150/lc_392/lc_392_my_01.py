def main(s, t):
    ns = len(s)
    nt = len(t)

    if ns > nt:
        return False

    slp, tlp = 0, 0
    srp, trp = ns - 1, nt - 1
    cnt = 0
    while slp < srp and tlp < trp:
        if s[slp] == t[tlp]:
            cnt += 1
            slp += 1
            tlp += 1
            continue
        if s[srp] == t[trp]:
            cnt += 1
            srp -= 1
            trp -= 1
            continue
        tlp += 1
        trp -= 1

    if slp == srp:
        i = tlp
        while i <= trp:
            if s[slp] == t[i]:
                cnt += 1
                break
            else:
                i += 1
    
    if cnt == ns:
        return True
    else:
        return False

if (__name__)==("__main__"):
    tc = [
            ["abc","ahbgdc"],
            ["axc","ahbgdc"]
    ]

    for t in tc:
        print(main(t[0], t[1]))
