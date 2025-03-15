from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
        Time Complexity: O(N), N = The number of nodes
        Space Complexity: O(1), 2 pointers
    """
    def hasCycleMy(self, head: Optional[ListNode]) -> bool:
        # Using current pointer (1 step) and forward pointer (2 steps)
        c_ptr, f_ptr = head, head

        while c_ptr and f_ptr:
            c_ptr = c_ptr.next
            
            if f_ptr.next:
                f_ptr = f_ptr.next.next
            else:
                return False
            
            if c_ptr == f_ptr:
                return True

        return False        

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False

def doTest():
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = head.next
        
    sol = Solution()
    result = sol.hasCycle(head)
    print(f"TC 1 Passed!" if result == True else "TC 1 Failed!")

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = head

    sol = Solution()
    result = sol.hasCycle(head)
    print(f"TC 2 Passed!" if result == True else "TC 2 Failed!")

    head = ListNode(1)
    sol = Solution()
    result = sol.hasCycle(head)
    print(f"TC 3 Passed!" if result == False else "TC 3 Failed!")    

doTest()