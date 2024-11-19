from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return 0
        
        op = { "+", "-", "*", "/"}
        st = []

        for v in tokens:
            if v not in op:
                st.append(int(v))
            else:
                y = st.pop()
                x = st.pop()
                if v == "+":
                    st.append(x + y)
                elif v == "-":
                    st.append(x - y)
                elif v == "*":
                    st.append(x * y)
                elif v == "/":
                    st.append(int(x / y))
        
        return st.pop()

tc = [
        [["2","1","+","3","*"], 9],
        [["4","13","5","/","+"], 6],
        [["10","6","9","3","+","-11","*","/","*","17","+","5","+"], 22]
    ]
sol = Solution()
for i in range(len(tc)):
    result = sol.evalRPN(tc[i][0])
    expected = tc[i][1]
    assert result == expected, "TC {} Failed - Expected: {}, Result: {}".format(i + 1, expected, result)
    print(f"TC {i + 1} Passed!")