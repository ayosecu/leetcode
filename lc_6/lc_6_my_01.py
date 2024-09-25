def main(s, numRows):
    if numRows == 1 or numRows >= len(s):
        return s

    idx, dir = 0, 1
    rows = [[] for _ in range(numRows)]

    for ch in s:
        rows[idx].append(ch)
        if idx == 0:
            dir = 1
        elif idx == numRows - 1:
            dir = -1
        idx += dir

    for i in range(numRows):
        rows[i] = ''.join(rows[i])

    return ''.join(rows)   

if (__name__)==("__main__"):
    tc = [
            ["PAYPALISHIRING", 3],
            ["PAYPALISHIRING", 4],
            ["A", 1]
    ]

    for t in tc:
        print(main(t[0], t[1]))