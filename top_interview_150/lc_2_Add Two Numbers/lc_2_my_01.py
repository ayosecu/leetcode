# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = ListNode()
        ptr = head
        
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
            ptr.next = ListNode(two_sum % 10)
            ptr = ptr.next

        if carry:
            ptr.next = ListNode(carry)
        
        return head.next

def convertList(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def doTest():
    sol = Solution()

    tc1_1 = ListNode(2)
    tc1_1.next = ListNode(4)
    tc1_1.next.next = ListNode(3)
    tc1_2 = ListNode(5)
    tc1_2.next = ListNode(6)
    tc1_2.next.next = ListNode(4)
    expect1 = [7, 0, 8]
    result1 = convertList(sol.addTwoNumbers(tc1_1, tc1_2))
    assert result1 == expect1, "TC1 Failed - Expected: {}, Result: {}".format(expect1, result1)
    print(result1)

doTest()