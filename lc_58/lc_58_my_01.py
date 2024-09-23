def main(s):
    n = len(s)

    count, i = 0, 0
    while i < n:
        if s[i] != " ":
            count += 1
        if i < n-1 and s[i] == " " and s[i+1] != " ":
            count = 0
        i += 1
    return count

if (__name__)==("__main__"):
    tc = [
        "Hello World",
        "   fly me   to   the moon  ",
        "luffy is still joyboy"
    ]

    for t in tc:
        print(main(t))
