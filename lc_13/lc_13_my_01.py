def main(s):
    dic = { "I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000 }
    n = len(s)
    sum, i = 0
    while i < n:
        if i < n-1 and s[i] == "I" and s[i+1] == 'V':
            sum += 4
            i += 1
        elif i < n-1 and s[i] == "I" and s[i+1] == "X":
            sum += 9
            i += 1
        elif i < n-1 and s[i] == "X" and s[i+1] == "L":
            sum += 40
            i += 1
        elif i < n-1 and s[i] == "X" and s[i+1] == "C":
            sum += 90
            i += 1
        elif i < n-1 and s[i] == "C" and s[i+1] == "D":
            sum += 400
            i += 1
        elif i < n-1 and s[i] == "C" and s[i+1] == "M":
            sum += 900
            i += 1
        else:
            sum += dic[s[i]]
        i += 1
    return sum

if (__name__)==("__main__"):
    tc = [
            "III",
            "LVIII",
            "MCMXCIV"
        ]

    for t in tc:
        print(main(t))