# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        new_head = Node(-1)
        ptr, prev = new_head.next, new_head
        random_ptr = []
        dic_ptr = {}

        i = 0
        while head:
            ptr = Node(head.val, head.next, head.random)
            dic_ptr[head] = i

            random_ptr.append(ptr)
            prev.next = ptr         

            head = head.next
            ptr = ptr.next
            prev = prev.next
            i += 1
       
        ptr = new_head.next
        i = 0
        while ptr:
            if ptr.random:
                ptr.random = random_ptr[dic_ptr[ptr.random]]
            ptr = ptr.next
        
        return new_head.next

def print_list(head):
    result = []
    while head:
        random_val = head.random.val if head.random else None
        result.append((head.val, random_val))
        head = head.next
    return result

def run_tests():
    solution = Solution()

    # Test case 1
    node1 = Node(1)
    node1.random = node1  # 자기 자신을 가리키는 random 포인터
    head1 = node1

    copied_head1 = solution.copyRandomList(head1)
    expected1 = [(1, 1)]
    result1 = print_list(copied_head1)
    print(f"Test 1 {'passed' if result1 == expected1 else 'failed'}: Expected {expected1}, Got {result1}")

    # Test case 2
    node2_1 = Node(1)
    node2_2 = Node(2)
    node2_1.next = node2_2
    node2_1.random = node2_2
    node2_2.random = node2_2
    head2 = node2_1

    copied_head2 = solution.copyRandomList(head2)
    expected2 = [(1, 2), (2, 2)]
    result2 = print_list(copied_head2)
    print(f"Test 2 {'passed' if result2 == expected2 else 'failed'}: Expected {expected2}, Got {result2}")

    # Test case 3
    node3_1 = Node(1)
    node3_2 = Node(2)
    node3_3 = Node(3)
    node3_1.next = node3_2
    node3_2.next = node3_3
    node3_1.random = node3_3
    node3_2.random = node3_1
    node3_3.random = node3_3
    head3 = node3_1

    copied_head3 = solution.copyRandomList(head3)
    expected3 = [(1, 3), (2, 1), (3, 3)]
    result3 = print_list(copied_head3)
    print(f"Test 3 {'passed' if result3 == expected3 else 'failed'}: Expected {expected3}, Got {result3}")

    # Test case 4
    head4 = None
    copied_head4 = solution.copyRandomList(head4)
    expected4 = []
    result4 = print_list(copied_head4)
    print(f"Test 4 {'passed' if result4 == expected4 else 'failed'}: Expected {expected4}, Got {result4}")

# Run the tests
run_tests()