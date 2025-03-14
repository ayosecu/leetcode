from typing import List
from collections import defaultdict, deque

class Solution:
    """
        - Time Complexity: O(N + P), N = numCourses, P = len(prerequisites)
        - Space Complexity: O(N + P), N = numCourses, P = len(prerequisites)
    """
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Topology Sort Algorithm
        ingress = [0] * numCourses
        edges = defaultdict(list)
        visited = set()

        for dst, src in prerequisites:
            ingress[dst] += 1
            edges[src].append(dst)       

        dq = deque([i for i in range(numCourses) if ingress[i] == 0])

        while dq:
            v = dq.popleft()
            visited.add(v)

            for e in edges[v]:
                ingress[e] -= 1
                if ingress[e] == 0:
                    dq.append(e)
        
        return numCourses == len(visited)


def run_tests():
    solution = Solution()

    # Test cases
    test_cases = [
        (2, [[1, 0]], True),                     # Simple case, one prerequisite
        (2, [[1, 0], [0, 1]], False),            # Cycle in prerequisites
        (4, [[1, 0], [2, 1], [3, 2]], True),     # Linear dependency
        (4, [[1, 0], [2, 1], [0, 2]], False),    # Cycle involving multiple courses
        (3, [], True),                           # No prerequisites
        (3, [[1, 0], [2, 0]], True),             # Multiple courses depending on one
        (5, [[1, 0], [2, 0], [3, 1], [4, 3]], True),  # Complex acyclic graph
    ]

    for i, (numCourses, prerequisites, expected) in enumerate(test_cases, 1):
        result = solution.canFinish(numCourses, prerequisites)
        print(f"Test case {i}: {'Passed' if result == expected else 'Failed'}, Result: {result}, Expected: {expected}")

# Run the tests
run_tests()