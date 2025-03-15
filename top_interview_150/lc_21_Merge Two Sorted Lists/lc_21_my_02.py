from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
        - Time Complexity: O(N+M), N = The number of list1's nodes, M = The number of list2's nodes.
        - Space Complexity: O(1), a merged_head node
    """
    def mergeTwoListsMy(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        
        if not list1 or not list2:
            return list1 if not list2 else list2
        
        merged_head = ListNode(-1)
        merged = merged_head
        
        while list1 and list2:
            if list1.val < list2.val:
                merged.next = list1
                list1 = list1.next
            else:
                merged.next = list2
                list2 = list2.next
            merged = merged.next
        
        while list1 or list2:
            merged.next = list1 if list1 else list2
            merged = merged.next
            if list1:
                list1 = list1.next
            else:
                list2 = list2.next
        
        return merged_head.next        
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy_h = dummy

        while list1 and list2:
            if list1.val < list2.val:
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next
            dummy = dummy.next
        
        if list1:
            dummy.next = list1
        else:
            dummy.next = list2
        
        return dummy_h.next

# Helper function to convert a list to a linked list
def list_to_linked(lst):
    dummy = ListNode()
    tail = dummy
    for num in lst:
        tail.next = ListNode(num)
        tail = tail.next
    return dummy.next

# Helper function to convert a linked list to a list
def linked_to_list(node):
    lst = []
    while node:
        lst.append(node.val)
        node = node.next
    return lst

# Test cases
def test_merge_two_lists():
    test_cases = [
        ([], [], []),
        ([1, 3, 5], [], [1, 3, 5]),
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6])
    ]

    sol = Solution()
    for i, (list1, list2, expected) in enumerate(test_cases):
        l1 = list_to_linked(list1)
        l2 = list_to_linked(list2)
        merged = sol.mergeTwoLists(l1, l2)
        result = linked_to_list(merged)
        assert result == expected, f"Test case {i+1} failed: {result} != {expected}"
        print(f"Test case {i+1} passed!")

test_merge_two_lists()