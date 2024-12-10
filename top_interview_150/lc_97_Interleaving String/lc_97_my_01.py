from collections import deque

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        n_s1, n_s2, n_s3 = len(s1), len(s2), len(s3)

        if n_s1 + n_s2 != n_s3:
            return False
        
        dq = deque([(0, 0)])
        visited = set()

        while dq:
            s1_idx, s2_idx = dq.popleft()

            if s1_idx + s2_idx == n_s3:
                return True
            
            if s1_idx < n_s1 and s1[s1_idx] == s3[s1_idx + s2_idx] and (s1_idx + 1, s2_idx) not in visited:
                dq.append((s1_idx + 1, s2_idx))
                visited.add((s1_idx + 1, s2_idx))
            if s2_idx < n_s2 and s2[s2_idx] == s3[s1_idx + s2_idx] and (s1_idx, s2_idx + 1) not in visited:
                dq.append((s1_idx, s2_idx + 1))
                visited.add((s1_idx, s2_idx + 1))
        
        return False

tc = [
        ("aabcc", "dbbca", "aadbbcbcac", True),
        ("aabcc", "dbbca", "aadbbbaccc", False),
        ("", "", "", True)
    ]

sol = Solution()
for i, t in enumerate(tc):
    result = sol.isInterleave(t[0], t[1], t[2])
    assert result == t[3], "TC {} Failed, Expected: {}, Result: {}".format(i + 1, t[3], result)
    print(f"TC {i + 1} Passed!")