def main(s):
    ret = ""
    w = s.split()
    for i in range(len(w)-1, -1, -1):
        ret += w[i]
        if i != 0:
            ret += " "
    return ret     

if (__name__)==("__main__"):
    tc = [
            "the sky is blue",
            "  hello world  ",
            "a good   example"
    ]

    for t in tc:
        print(main(t))