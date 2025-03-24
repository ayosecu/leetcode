from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
        - Time Complexity: O(n), n = the number of nodes.
        - Space Complexity: O(1)
    """
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        dummy = ListNode(-1)
        dummy.next = head

        before_ptr = dummy
        for _ in range(left - 1):
            before_ptr = before_ptr.next
        
        new_next = None
        current = before_ptr.next
        for _ in range(right - left + 1):
            next_ptr = current.next
            current.next = new_next
            new_next = current
            current = next_ptr
        
        before_ptr.next.next = current
        before_ptr.next = new_next

        return dummy.next

def list_to_linked_list(elements):
    """Convert a list to a linked list."""
    dummy = ListNode(0)
    current = dummy
    for element in elements:
        current.next = ListNode(element)
        current = current.next
    return dummy.next

def linked_list_to_list(head):
    """Convert a linked list to a list."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def run_tests():
    solution = Solution()

    # Test case 1: Reverse middle part
    head1 = list_to_linked_list([1, 2, 3, 4, 5])
    left1, right1 = 2, 4
    expected1 = [1, 4, 3, 2, 5]
    result1 = linked_list_to_list(solution.reverseBetween(head1, left1, right1))
    print(f"Test 1 {'passed' if result1 == expected1 else 'failed'}: Expected {expected1}, Got {result1}")

    # Test case 2: Reverse entire list
    head2 = list_to_linked_list([1, 2, 3, 4, 5])
    left2, right2 = 1, 5
    expected2 = [5, 4, 3, 2, 1]
    result2 = linked_list_to_list(solution.reverseBetween(head2, left2, right2))
    print(f"Test 2 {'passed' if result2 == expected2 else 'failed'}: Expected {expected2}, Got {result2}")

    # Test case 3: Reverse single node
    head3 = list_to_linked_list([1, 2, 3, 4, 5])
    left3, right3 = 3, 3
    expected3 = [1, 2, 3, 4, 5]
    result3 = linked_list_to_list(solution.reverseBetween(head3, left3, right3))
    print(f"Test 3 {'passed' if result3 == expected3 else 'failed'}: Expected {expected3}, Got {result3}")

    # Test case 4: Reverse part of the list at the end
    head4 = list_to_linked_list([1, 2, 3, 4, 5])
    left4, right4 = 4, 5
    expected4 = [1, 2, 3, 5, 4]
    result4 = linked_list_to_list(solution.reverseBetween(head4, left4, right4))
    print(f"Test 4 {'passed' if result4 == expected4 else 'failed'}: Expected {expected4}, Got {result4}")

    # Test case 5: Single node list
    head5 = list_to_linked_list([1])
    left5, right5 = 1, 1
    expected5 = [1]
    result5 = linked_list_to_list(solution.reverseBetween(head5, left5, right5))
    print(f"Test 5 {'passed' if result5 == expected5 else 'failed'}: Expected {expected5}, Got {result5}")

# Run the tests
run_tests()    