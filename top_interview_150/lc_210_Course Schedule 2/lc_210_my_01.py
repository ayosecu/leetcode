from typing import List
from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        dic = defaultdict(list)
        ingress = [0] * numCourses

        for dst, src in prerequisites:
            dic[src].append(dst)
            ingress[dst] += 1
        
        dq = deque([ i for i in range(numCourses) if ingress[i] == 0])
        visited = []

        while dq:
            pop_node = dq.popleft()
            visited.append(pop_node)

            for dst in dic[pop_node]:
                ingress[dst] -= 1
                if ingress[dst] == 0:
                    dq.append(dst)
        
        return visited if len(visited) == numCourses else []


tc = [
        (2, [[1,0]], [0, 1]),
        (4, [[1,0],[2,0],[3,1],[3,2]], [0,1,2,3]),
        (1, [], [0])
    ]

for i, (num, pre, expected) in enumerate(tc, 1):
    sol = Solution()
    result = sol.findOrder(num, pre)
    assert result == expected, "TC {} Failed!! - Expected: {}, Result: {}".format(i, expected, result)
    print(f"TC {i} Passed!!")