# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        # Dummy 1 (less list) : 1 -> 2 ->2
        d1_head = ListNode()
        d1_cur = d1_head
        # Dummy 2 (greater list) : 4 -> 3 -> 5 -> None
        d2_head = ListNode()
        d2_cur = d2_head
        
        while head:
            if head.val < x:
                d1_cur.next = head
                d1_cur = d1_cur.next
            else:
                d2_cur.next = head
                d2_cur = d2_cur.next

            head = head.next
        
        d2_cur.next = None
        d1_cur.next = d2_head.next

        return d1_head.next


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
        ([1, 4, 3, 2, 5, 2], 3, [1, 2, 2, 4, 3, 5]),  # General case
        ([2, 1], 2, [1, 2]),                         # All elements are less or equal to x
        ([5, 6, 7], 3, [5, 6, 7]),                   # All elements are greater than x
        ([1, 2, 3], 4, [1, 2, 3]),                   # All elements are less than x
        ([], 0, []),                                 # Empty list
        ([1], 0, [1]),                               # Single element
    ]

    for i, (values, x, expected) in enumerate(test_cases, 1):
        head = create_linked_list(values)
        result = solution.partition(head, x)
        result_list = linked_list_to_list(result)
        print(f"Test case {i}: {'Passed' if result_list == expected else 'Failed'}, Result: {result_list}, Expected: {expected}")

# Run the tests
run_tests()