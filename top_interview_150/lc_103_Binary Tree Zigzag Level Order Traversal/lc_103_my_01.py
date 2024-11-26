from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def zigzagLevelOrderMy(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []

        result = []
        st = []
        st.append(root)

        order = 1
        while st:
            level_list = []
            temp_q = []

            while st:
                temp_q.append(st.pop())
            while temp_q:                
                pop_node = temp_q.pop(0)
                level_list.append(pop_node.val)
                if order == 1:
                    if pop_node.left:
                        st.append(pop_node.left)
                    if pop_node.right:
                        st.append(pop_node.right)
                else:
                    if pop_node.right:
                        st.append(pop_node.right)
                    if pop_node.left:
                        st.append(pop_node.left)
            result.append(level_list)
            order *= -1
       
        return result

    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []

        result = []        
        dq = deque([root])
        left_to_right = True

        while dq:
            level_list = []

            for _ in range(len(dq)):
                pop_node = dq.popleft()
                level_list.append(pop_node.val)

                if pop_node.left:
                    dq.append(pop_node.left)
                if pop_node.right:
                    dq.append(pop_node.right)
            
            if not left_to_right:
                level_list.reverse()
            
            result.append(level_list)
            left_to_right = not left_to_right

        return result

def list_to_tree_node(values):
    """Convert a list to a binary tree using level order."""
    if not values:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        if values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root

def run_tests():
    solution = Solution()

    # Test case 1: 기본적인 이진 트리
    root1 = list_to_tree_node([3, 9, 20, None, None, 15, 7])
    expected1 = [[3], [20, 9], [15, 7]]
    result1 = solution.zigzagLevelOrder(root1)
    print(f"Test 1 {'passed' if result1 == expected1 else 'failed'}: Expected {expected1}, Got {result1}")

    # Test case 2: 단일 노드 트리
    root2 = list_to_tree_node([1])
    expected2 = [[1]]
    result2 = solution.zigzagLevelOrder(root2)
    print(f"Test 2 {'passed' if result2 == expected2 else 'failed'}: Expected {expected2}, Got {result2}")

    # Test case 3: 빈 트리
    root3 = list_to_tree_node([])
    expected3 = []
    result3 = solution.zigzagLevelOrder(root3)
    print(f"Test 3 {'passed' if result3 == expected3 else 'failed'}: Expected {expected3}, Got {result3}")

    # Test case 4: 왼쪽에만 노드가 있는 트리
    root4 = list_to_tree_node([1, 2, None, 3])
    expected4 = [[1], [2], [3]]
    result4 = solution.zigzagLevelOrder(root4)
    print(f"Test 4 {'passed' if result4 == expected4 else 'failed'}: Expected {expected4}, Got {result4}")

    # Test case 5: 오른쪽에만 노드가 있는 트리
    root5 = list_to_tree_node([1, None, 2, None, 3])
    expected5 = [[1], [2], [3]]
    result5 = solution.zigzagLevelOrder(root5)
    print(f"Test 5 {'passed' if result5 == expected5 else 'failed'}: Expected {expected5}, Got {result5}")

# Run the tests
run_tests()