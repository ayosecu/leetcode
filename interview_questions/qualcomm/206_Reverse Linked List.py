from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
        - Time Complexity: O(n), n = The number of nodes.
        - Space Complexity: O(1)
    """
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # two pointers : forward & current
        if not head:
            return head

        current = head
        forward = head.next

        while forward:
            next_forward = forward.next
            forward.next = current

            current = forward
            forward = next_forward
        
        head.next = None

        return current

class SolutionRecursive:
    """
        - Time Complexity: O(n), n = The number of nodes.
        - Space Complexity: O(n), calling n times in recursive (stack).
    """
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # recursive
        if not head or not head.next:
            return head

        next_node = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return next_node

# Function to create a linked list from a list
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Function to convert linked list to list (for easy comparison)
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def run_tests():
    solution = Solution()  # Iterative solution
    solution_recursive = SolutionRecursive()  # Recursive solution

    test_cases = [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),  # Normal case
        ([1], [1]),  # Single node
        ([], []),  # Empty list
        ([1, 2], [2, 1]),  # Two elements
        ([10, 20, 30, 40], [40, 30, 20, 10]),  # Even number of elements
    ]

    for i, (input_list, expected) in enumerate(test_cases, 1):
        head = create_linked_list(input_list)

        # Iterative test
        result_iterative = linked_list_to_list(solution.reverseList(create_linked_list(input_list)))
        print(f"Test case {i} (Iterative): {'Passed' if result_iterative == expected else 'Failed'}")
        print(f"  Input: {input_list}")
        print(f"  Output: {result_iterative}")
        print(f"  Expected: {expected}\n")

        # Recursive test
        result_recursive = linked_list_to_list(solution_recursive.reverseList(create_linked_list(input_list)))
        print(f"Test case {i} (Recursive): {'Passed' if result_recursive == expected else 'Failed'}")
        print(f"  Output: {result_recursive}")
        print(f"  Expected: {expected}\n")

# Run the tests
run_tests()