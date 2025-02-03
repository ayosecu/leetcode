class Solution:
    """
        - Time Complexity: O(n), n = len(path)
        - Space Complexity: O(n), n = len(path)
    """
    def simplifyPath(self, path: str) -> str:
        st = []

        for s in path.split("/"):
            if s == "..":
                if st:
                    st.pop()
                continue
            if s == "." or s == "":
                continue
            st.append(s)
        
        return "/" + "/".join(st)

tc = [
        ("/home/", "/home"),
        ("/home//foo/", "/home/foo"),
        ("/home/user/Documents/../Pictures", "/home/user/Pictures"),
        ("/../", "/"),
        ("/.../a/../b/c/../d/./", "/.../b/d")
    ]

for i, (t, e) in enumerate(tc, 1):
    sol = Solution()
    r = sol.simplifyPath(t)
    print(f"TC {i} Passed!!" if r == e else f"TC {i} Failed!! - Expected:{e}, Result: {r}")