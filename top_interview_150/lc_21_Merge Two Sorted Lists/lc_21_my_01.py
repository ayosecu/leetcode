# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 is None and list2 is None:
            return None

        merged_list = ListNode()
        add_ptr = merged_list
        while list1 and list2:
            if list1.val < list2.val:
                add_ptr.next = ListNode(list1.val)
                list1 = list1.next                
            else:
                add_ptr.next = ListNode(list2.val)
                list2 = list2.next
            add_ptr = add_ptr.next

        while list1:
            add_ptr.next = ListNode(list1.val)
            list1 = list1.next
            add_ptr = add_ptr.next      

        while list2:
            add_ptr.next = ListNode(list2.val)
            list2 = list2.next
            add_ptr = add_ptr.next

        return merged_list.next
        

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