from collections import defaultdict, deque

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # Topological Sort
        course_dic = defaultdict(list)
        ingress = [0] * numCourses

        for dst, src in prerequisites:
            course_dic[src].append(dst)
            ingress[dst] += 1
        
        dq = deque([i for i in range(numCourses) if ingress[i] == 0])
        visited_count = 0

        while dq:
            visited = dq.popleft()
            visited_count += 1

            for neighbor in course_dic[visited]:
                ingress[neighbor] -= 1
                if ingress[neighbor] == 0:
                    dq.append(neighbor)
        
        return visited_count == numCourses



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