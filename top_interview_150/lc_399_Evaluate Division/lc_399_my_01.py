from collections import defaultdict, deque

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        dic = defaultdict(list)
        for (x, y), v in zip(equations, values):
            dic[x].append((y, v))
            dic[y].append((x, 1 / v))
        
        def bfs(start, end):
            if start not in dic or end not in dic:
                return -1.0
            if start == end:
                return 1.0
            
            dq = deque([(start, 1.0)])
            visited = set()

            while dq:
                current, val = dq.popleft()
                visited.add(current)

                if current == end:
                    return val
                
                for neighbor, v in dic[current]:
                    if neighbor not in visited:
                        dq.append((neighbor, val * v))

            return -1.0

        return [bfs(x, y) for (x, y) in queries]

def run_tests():
    solution = Solution()

    # Test case 1
    equations1 = [["a", "b"], ["b", "c"]]
    values1 = [2.0, 3.0]
    queries1 = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    expected1 = [6.0, 0.5, -1.0, 1.0, -1.0]
    result1 = solution.calcEquation(equations1, values1, queries1)
    print(f"Test 1 {'passed' if result1 == expected1 else 'failed'}: Expected {expected1}, Got {result1}")

    # Test case 2
    equations2 = [["a", "b"], ["c", "d"]]
    values2 = [1.5, 2.5]
    queries2 = [["a", "b"], ["c", "d"], ["a", "d"], ["b", "c"]]
    expected2 = [1.5, 2.5, -1.0, -1.0]
    result2 = solution.calcEquation(equations2, values2, queries2)
    print(f"Test 2 {'passed' if result2 == expected2 else 'failed'}: Expected {expected2}, Got {result2}")

    # Test case 3
    equations3 = [["a", "b"], ["b", "c"]]
    values3 = [2.0, 3.0]
    queries3 = [["a", "a"], ["b", "b"], ["c", "c"]]
    expected3 = [1.0, 1.0, 1.0]
    result3 = solution.calcEquation(equations3, values3, queries3)
    print(f"Test 3 {'passed' if result3 == expected3 else 'failed'}: Expected {expected3}, Got {result3}")

    # Test case 4
    equations4 = [["a", "b"]]
    values4 = [4.0]
    queries4 = [["a", "b"], ["b", "a"], ["a", "c"]]
    expected4 = [4.0, 0.25, -1.0]
    result4 = solution.calcEquation(equations4, values4, queries4)
    print(f"Test 4 {'passed' if result4 == expected4 else 'failed'}: Expected {expected4}, Got {result4}")

    # Test case 5:
    equations5 = []
    values5 = []
    queries5 = [["a", "b"]]
    expected5 = [-1.0]
    result5 = solution.calcEquation(equations5, values5, queries5)
    print(f"Test 5 {'passed' if result5 == expected5 else 'failed'}: Expected {expected5}, Got {result5}")

# Run the tests
run_tests()
