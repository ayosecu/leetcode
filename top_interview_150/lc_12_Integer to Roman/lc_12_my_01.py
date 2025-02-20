def main(num):
    ret = ""
    dic = { 1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M",
            4:"IV", 9:"IX", 40:"XL", 90:"XC", 400:"CD", 900:"CM" }

    for i in range(3, -1, -1):
        n = num // (10**i)
        if i == 3:
            for j in range(n):
                ret += dic[1000]
            num -= n*1000
        elif i == 2:
            if n < 4:
                for j in range(n):
                    ret += dic[100]
            elif n == 4 or n == 5:
                ret += dic[n*100]
            elif n > 5 and n < 9:
                ret += dic[500]
                k = n - 5
                for j in range(k):
                    ret += dic[100]
            elif n == 9:
                ret += dic[900]
            num -= n*100       
        elif i == 1:
            if n < 4:
                for j in range(n):
                    ret += dic[10]
            elif n == 4 or n == 5:
                ret += dic[n*10]
            elif n > 5 and n < 9:
                ret += dic[50]
                k = n - 5
                for j in range(k):
                    ret += dic[10]
            elif n == 9:
                ret += dic[90]
            num -= n*10     
        elif i == 0:
            if n < 4:
                for j in range(n):
                    ret += dic[1]
            elif n == 4 or n == 5:
                ret += dic[n]
            elif n > 5 and n < 9:
                ret += dic[5]
                k = n - 5
                for j in range(k):
                    ret += dic[1]
            elif n == 9:
                ret += dic[9]
            num -= n
    return ret

if (__name__)==("__main__"):
    tc = [3749, 58, 1994]
    for t in tc:
        print(main(t))