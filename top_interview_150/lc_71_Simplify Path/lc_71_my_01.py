class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """        
        s_list = path.split("/")
        result_q = []

        for w in s_list:
            if w == "..":
                if result_q:
                    result_q.pop()
                continue
            if w == "." or w == "":
                continue            
            result_q.append(w)
        
        result = "/" + "/".join(result_q)
        return result

tc = [
        "/home/",
        "/home//foo/",
        "/home/user/Documents/../Pictures",
        "/../",
        "/.../a/../b/c/../d/./"
    ]

sol = Solution()
for t in tc:
    print(sol.simplifyPath(t))