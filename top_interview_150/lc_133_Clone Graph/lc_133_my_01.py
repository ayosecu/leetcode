from collections import deque, defaultdict

# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None

        dq = deque([node])
        dic = defaultdict(None)
        dic[node.val] = Node(node.val)

        while dq:
            pop_node = dq.popleft()
            for n in pop_node.neighbors:               
                if n.val not in dic:
                    dic[n.val] = Node(n.val)
                    dq.append(n)
                dic[pop_node.val].neighbors.append(dic[n.val])
        
        return dic[node.val]

def print_graph(node):
    if not node:
        return []

    visited = set()
    result = []
    queue = deque([node])

    while queue:
        current = queue.popleft()
        if current in visited:
            continue
        visited.add(current)
        result.append((current.val, sorted([neighbor.val for neighbor in current.neighbors])))
        for neighbor in current.neighbors:
            if neighbor not in visited:
                queue.append(neighbor)

    return sorted(result, key=lambda x: x[0])

def run_tests():
    solution = Solution()

    # Test case 1
    node1 = Node(1)
    cloned_graph1 = solution.cloneGraph(node1)
    expected1 = [(1, [])]
    result1 = print_graph(cloned_graph1)
    print(f"Test 1 {'passed' if result1 == expected1 else 'failed'}: Expected {expected1}, Got {result1}")

    # Test case 2
    node2_1 = Node(1)
    node2_2 = Node(2)
    node2_1.neighbors.append(node2_2)
    node2_2.neighbors.append(node2_1)
    cloned_graph2 = solution.cloneGraph(node2_1)
    expected2 = [(1, [2]), (2, [1])]
    result2 = print_graph(cloned_graph2)
    print(f"Test 2 {'passed' if result2 == expected2 else 'failed'}: Expected {expected2}, Got {result2}")

    # Test case 3
    node3_1 = Node(1)
    node3_2 = Node(2)
    node3_3 = Node(3)
    node3_4 = Node(4)
    node3_1.neighbors = [node3_2, node3_4]
    node3_2.neighbors = [node3_1, node3_3]
    node3_3.neighbors = [node3_2, node3_4]
    node3_4.neighbors = [node3_1, node3_3]
    cloned_graph3 = solution.cloneGraph(node3_1)
    expected3 = [(1, [2, 4]), (2, [1, 3]), (3, [2, 4]), (4, [1, 3])]
    result3 = print_graph(cloned_graph3)
    print(f"Test 3 {'passed' if result3 == expected3 else 'failed'}: Expected {expected3}, Got {result3}")

    # Test case 4
    node4 = None
    cloned_graph4 = solution.cloneGraph(node4)
    expected4 = []
    result4 = print_graph(cloned_graph4)
    print(f"Test 4 {'passed' if result4 == expected4 else 'failed'}: Expected {expected4}, Got {result4}")

# Run the tests
run_tests()