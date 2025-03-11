from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
        - Time Complexity : O(N + M), N = The number of headA list, M = The number of headB list.
        - Space Complexity : O(N), N = The number of headA list
    """
    def getIntersectionNodeHash(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        node_set = set()

        while headA:
            node_set.add(headA)
            headA = headA.next
        
        while headB:
            if headB in node_set:
                return headB
            headB = headB.next

        return None

    """
        - Time Complexity : O(N + M), N = The number of headA list, M = The number of headB list.
        - Space Complexity : O(1), ptrA, ptrB
    """
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:        
        ptrA = headA
        ptrB = headB

        while ptrA != ptrB:
            ptrA = ptrA.next if ptrA else headB
            ptrB = ptrB.next if ptrB else headA
        
        return ptrA


# Function to create a linked list from a list and return head
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Function to find a node in a linked list
def find_node(head, val):
    while head and head.val != val:
        head = head.next
    return head

# Function to print linked list from a given node
def print_linked_list(head):
    result = []
    while head:
        result.append(str(head.val))
        head = head.next
    print(" -> ".join(result))

def run_tests():
    solution = Solution()

    # Test case 1: Intersection at node with value 8
    """
    A: 4 -> 1 \
                8 -> 4 -> 5
    B:     5 -> 6 -> 1 /
    """
    common = create_linked_list([8, 4, 5])
    headA = create_linked_list([4, 1])
    headB = create_linked_list([5, 6, 1])

    # Connect the intersection
    find_node(headA, 1).next = common
    find_node(headB, 1).next = common

    expected = 8
    result = solution.getIntersectionNode(headA, headB)
    print(f"Test Case 1: {'Passed' if (result and result.val == expected) else 'Failed'}")
    print(f"  Intersection Node: {result.val if result else None}")

    # Test case 2: No intersection
    """
    A: 1 -> 2 -> 3
    B: 4 -> 5 -> 6
    """
    headA = create_linked_list([1, 2, 3])
    headB = create_linked_list([4, 5, 6])

    expected = None
    result = solution.getIntersectionNode(headA, headB)
    print(f"Test Case 2: {'Passed' if result == expected else 'Failed'}")
    print(f"  Intersection Node: {result.val if result else None}")

    # Test case 3: Intersection at head
    """
    A: 1 -> 2 -> 3
    B: 1 -> 2 -> 3
    """
    headA = create_linked_list([1, 2, 3])
    headB = headA  # Same reference

    expected = 1
    result = solution.getIntersectionNode(headA, headB)
    print(f"Test Case 3: {'Passed' if (result and result.val == expected) else 'Failed'}")
    print(f"  Intersection Node: {result.val if result else None}")

    # Test case 4: Both lists are empty
    """
    A: None
    B: None
    """
    headA = None
    headB = None

    expected = None
    result = solution.getIntersectionNode(headA, headB)
    print(f"Test Case 4: {'Passed' if result == expected else 'Failed'}")
    print(f"  Intersection Node: {result.val if result else None}")

    # Test case 5: Intersection at last node
    """
    A: 2 -> 6 -> 4
    B: 1 -> 5 -> 4
    """
    common = create_linked_list([4])
    headA = create_linked_list([2, 6])
    headB = create_linked_list([1, 5])

    # Connect the intersection
    find_node(headA, 6).next = common
    find_node(headB, 5).next = common

    expected = 4
    result = solution.getIntersectionNode(headA, headB)
    print(f"Test Case 5: {'Passed' if (result and result.val == expected) else 'Failed'}")
    print(f"  Intersection Node: {result.val if result else None}")

# Run the tests
run_tests()