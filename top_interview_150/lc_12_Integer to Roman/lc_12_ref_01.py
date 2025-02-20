def main(num):
    ret = ""
    
    num_sort = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    s_sort = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    i = 0
    while num > 0:
        if num >= num_sort[i]:
            ret += s_sort[i]
            num -= num_sort[i]
        else:
            i += 1
    return ret

if (__name__)==("__main__"):
    tc = [3749, 58, 1994]
    for t in tc:
        print(main(t))