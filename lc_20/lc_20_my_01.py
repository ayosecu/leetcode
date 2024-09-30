def main(s):
    o_list = {"(", "[", "{"}
    st = []

    for ch in s:
        if ch in o_list:
            st.append(ch)
        else:
            if len(st) < 1:
                return False            
            c = st.pop()
            if ch == ")" and c != "(":
                return False
            elif ch == "]" and c != "[":
                return False
            elif ch == "}" and c != "{":
                return False            

    return True if len(st) == 0 else False

if (__name__)==("__main__"):
    tc = [
            "()",
            "()[]{}",
            "(]",
            "([])",
            "[",
            "]"
    ]

    for t in tc:
        print(main(t))