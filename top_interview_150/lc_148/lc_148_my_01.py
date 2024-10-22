# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def findMid(node):
            slow = node
            fast = node
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next           
            return slow
        
        def merge(left, right):
            sorted_head = ListNode()
            ptr = sorted_head

            while left and right:
                if left.val <= right.val:
                    ptr.next = left
                    left = left.next
                else:
                    ptr.next = right
                    right = right.next
                ptr = ptr.next
            if left:
                ptr.next = left
            if right:
                ptr.next = right
            
            return sorted_head.next

        def mergeSort(node):
            if not node or not node.next:
                return node
            
            mid = findMid(node)
            next_mid = mid.next
            mid.next = None
            left = mergeSort(node)
            right = mergeSort(next_mid)
            
            return merge(left, right)
        
        return mergeSort(head)

            
# 테스트 케이스
def list_to_linkedlist(arr):
    """ 리스트를 Linked List로 변환하는 함수 """
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linkedlist_to_list(node):
    """ Linked List를 리스트로 변환하는 함수 """
    result = []
    current = node
    while current:
        result.append(current.val)
        current = current.next
    return result

# 테스트 실행
if __name__ == "__main__":
    # 테스트 케이스 1
    input_list = [4, 2, 1, 3]
    head = list_to_linkedlist(input_list)
    solution = Solution()
    sorted_head = solution.sortList(head)
    sorted_list = linkedlist_to_list(sorted_head)
    print("Test case 1: ", sorted_list)  # 출력: [1, 2, 3, 4]

    # 테스트 케이스 2
    input_list = [-1, 5, 3, 4, 0]
    head = list_to_linkedlist(input_list)
    sorted_head = solution.sortList(head)
    sorted_list = linkedlist_to_list(sorted_head)
    print("Test case 2: ", sorted_list)  # 출력: [-1, 0, 3, 4, 5]

    # 테스트 케이스 3 (빈 리스트)
    input_list = []
    head = list_to_linkedlist(input_list)
    sorted_head = solution.sortList(head)
    sorted_list = linkedlist_to_list(sorted_head)
    print("Test case 3: ", sorted_list)  # 출력: []

    # 테스트 케이스 4 (이미 정렬된 리스트)
    input_list = [1, 2, 3, 4]
    head = list_to_linkedlist(input_list)
    sorted_head = solution.sortList(head)
    sorted_list = linkedlist_to_list(sorted_head)
    print("Test case 4: ", sorted_list)  # 출력: [1, 2, 3, 4]        