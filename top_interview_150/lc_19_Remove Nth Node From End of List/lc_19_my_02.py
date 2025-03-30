from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
        - Time Complexity: O(n)
        - Space Complexity: O(n)
    """
    def removeNthFromEndList(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node_list = []

        dummy = ListNode(-1)
        dummy.next = head
        node_list.append(dummy)

        cnt = 0
        current = head
        while current:
            node_list.append(current)
            cnt += 1
            current = current.next
        
        target_idx = cnt - n + 1
        node_list[target_idx - 1].next = node_list[target_idx].next

        return dummy.next

    """
        - Time Complexity: O(n)
        - Space Complexity: O(1)
    """
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        
        slow, fast = dummy, dummy
        for _ in range(n + 1):
            fast = fast.next
        
        while fast:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next

        return dummy.next

        
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
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),  # Remove 2nd node from the end
        ([1], 1, []),                        # Remove the only node
        ([1, 2], 1, [1]),                   # Remove the last node
        ([1, 2], 2, [2]),                   # Remove the head node
    ]

    for i, (values, n, expected) in enumerate(test_cases, 1):
        head = create_linked_list(values)
        result = solution.removeNthFromEnd(head, n)
        result_list = linked_list_to_list(result)
        print(f"Test case {i}: {'Passed' if result_list == expected else 'Failed'}, Result: {result_list}, Expected: {expected}")

# Run the tests
run_tests()