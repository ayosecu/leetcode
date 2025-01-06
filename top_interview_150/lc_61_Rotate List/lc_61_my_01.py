# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or k == 0:
            return head
        
        node_cnt = 1
        ptr = head
        while ptr.next:
            node_cnt += 1
            ptr = ptr.next

        # make circular
        ptr.next = head
        k = k % node_cnt 
        new_tail_idx = node_cnt - k - 1
        for _ in range(new_tail_idx):
            head = head.next

        new_head = head.next
        head.next = None

        return new_head

    def rotateRightList(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or k == 0:
            return head

        node_map = []
        ptr = head
        while ptr:
            node_map.append(ptr)
            ptr = ptr.next

        # make circular
        node_map[-1].next = node_map[0]

        # mod k
        k = k % len(node_map)
        # new tail : before -k
        node_map[-(k+1)].next = None

        return node_map[-k]

def create_linked_list(values):
    """Helper function to create a linked list from a list of values."""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head):
    """Helper function to convert a linked list back to a list."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def run_tests():
    solution = Solution()

    # Test cases
    test_cases = [
        ([1, 2, 3, 4, 5], 2, [4, 5, 1, 2, 3]),  # General case
        ([0, 1, 2], 4, [2, 0, 1]),              # k > length of list
        ([], 1, []),                            # Empty list
        ([1], 0, [1]),                          # Single node, no rotation
        ([1], 2, [1]),                          # Single node, any k
        ([1, 2], 2, [1, 2]),                   # k == length of list
    ]

    for i, (values, k, expected) in enumerate(test_cases, 1):
        head = create_linked_list(values)
        rotated_head = solution.rotateRight(head, k)
        result = linked_list_to_list(rotated_head)
        print(f"Test case {i}: {'Passed' if result == expected else 'Failed'}, Result: {result}, Expected: {expected}")

# Run the tests
run_tests()