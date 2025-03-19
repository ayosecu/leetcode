from typing import List

class Solution:
    """
        - Time Complexity: O(n), n = len(tokens)
        - Space Complexity: O(N), in worst O(n) 
            - N = The number of operands.
            - N is at most n/2 => O(n/2) => O(n)
    """
    def evalRPN(self, tokens: List[str]) -> int:
        op = {"+", "-", "*", "/"}
        st = []
        
        for c in tokens:
            if c in op and len(st) >= 2:
                second = st.pop()
                first = st.pop()
                if c == "+":
                    st.append(first + second)
                elif c == "-":
                    st.append(first - second)
                elif c == "*":
                    st.append(first * second)
                elif c == "/":
                    st.append(int(first / second))
            else:
                st.append(int(c))
        
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