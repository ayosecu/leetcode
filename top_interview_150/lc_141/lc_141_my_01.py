# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False          
        ptr = head
        checkNode = ListNode(-1)
        while ptr.next != None:
            if ptr.next == checkNode:
                return True
            tmp = ptr.next
            ptr.next = checkNode
            ptr = tmp

        return False

if (__name__)==("__main__"):
    tc = [
            [[3, 2, 0, -4], 1],
            [[1, 2], 0],
            [[1], -1]
    ]

    for t in tc:
        head = None
        prev = None
        pos = None
        n = len(t[0])
        for i in range(n):
            ptr = ListNode(t[0][i])
            if i == 0:
                head = ptr
            else:
                prev.next = ptr           
            if i == t[1]:
                pos = ptr
            if i == n - 1:
                ptr.next = pos           
            prev = ptr
        
        sol = Solution()
        print(sol.hasCycle(head))

            