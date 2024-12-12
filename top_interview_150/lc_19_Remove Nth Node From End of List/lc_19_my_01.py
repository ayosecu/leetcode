# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEndTwoPass(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        # 2 pass
        ptr = head
        size = 0
        while ptr:
            size += 1
            ptr = ptr.next
        
        if size < n or size <= 1:
            return None
        
        idx = size - n

        temp_node = ListNode(-1)
        temp_node.next = head
        prev = temp_node
        for _ in range(idx):
            prev = prev.next

        prev.next = prev.next.next

        return temp_node.next

    def removeNthFromEndOnePassList(self, head, n):
        ptr_list = []
        tmp = ListNode(-1)
        tmp.next = head
        ptr_list.append(tmp)

        ptr = head
        cnt = 0
        while ptr:
            ptr_list.append(ptr)
            ptr = ptr.next
            cnt += 1
        
        if cnt < n or cnt <= 1:
            return None
        
        prev = ptr_list[cnt - n]
        prev.next = prev.next.next

        return ptr_list[0].next

    def removeNthFromEnd(self, head, n):
        dummy = ListNode(-1)
        dummy.next = head

        front, back = dummy, dummy
        for _ in range(n + 1):
            front = front.next
        
        while front:
            front = front.next
            back = back.next
        back.next = back.next.next

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
