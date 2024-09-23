def main(s):
    w = s.rsplit(maxsplit=1)[-1]
    return len(w)

if (__name__)==("__main__"):
    tc = [
        "Hello World",
        "   fly me   to   the moon  ",
        "luffy is still joyboy"
    ]

    for t in tc:
        print(main(t))
