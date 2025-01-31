from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
        - Time Complexity: O(n), n = max(len(l1), len(l2))
        - Space Complexity: O(n), n = max(len(l1), len(l2))
    """
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode(-1)
        dummy = l3

        carry = 0
        while l1 or l2:
            two_sum = carry

            if l1:
                two_sum += l1.val
                l1 = l1.next
            
            if l2:
                two_sum += l2.val
                l2 = l2.next
            
            carry = two_sum // 10
            remain = two_sum % 10
            l3.next = ListNode(remain)
            l3 = l3.next
        
        if carry:
            l3.next = ListNode(carry)

        return dummy.next
    
def convertList(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def makeLinkedList(l):
    dummy = ListNode(-1)
    ptr = dummy
    for num in l:
        ptr.next = ListNode(num)
        ptr = ptr.next
    return dummy.next

def doTest():
    sol = Solution()

    tc = [
            ([2,4,3], [5,6,4], [7,0,8]),
            ([0], [0], [0]),
            ([9,9,9,9,9,9,9], [9,9,9,9], [8,9,9,9,0,0,0,1])
    ]

    for i, (l1, l2, expected) in enumerate(tc, 1):
        result = convertList(sol.addTwoNumbers(makeLinkedList(l1), makeLinkedList(l2)))
        print(f"TC {i} Passed!!" if result == expected else f"TC {i} Failed!! - Expected: {expected}, Result: {result}")
    
doTest()