# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return None
        
        # dummy / prev -> (head) 1 -> 2 -> 3 -> 3 -> 4 -> 4-> 5

        dummy = ListNode(-1, head)
        prev = dummy

        while prev.next:
            if prev.next.next and prev.next.next.val == prev.next.val:
                chk_ptr = prev.next.next
                while chk_ptr.next and chk_ptr.val == chk_ptr.next.val:
                    chk_ptr = chk_ptr.next
                prev.next = chk_ptr.next
            else:
                prev = prev.next
        
        return dummy.next

def linkedListToList(head):
    list = []
    while head:
        list.append(head.val)
        head = head.next
    return list

def run_test():
    sol = Solution()

    tc = [
            ( ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4, ListNode(5))))))), [1, 2, 5] ),
            ( ListNode(1, ListNode(1, ListNode(1, ListNode(2, ListNode(3))))), [2, 3]),
            ( None, [] )
        ]
    
    for i, t in enumerate(tc, 1):
        ret = linkedListToList(sol.deleteDuplicates(t[0]))
        assert ret == t[1], "TC {} Failed - Expected: {}, Return: {}".format(i, t[1], ret) 
        print(f"TC {i} Passed!")

run_test()



