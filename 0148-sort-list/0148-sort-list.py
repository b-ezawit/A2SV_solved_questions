# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def mergeCombine(leftLL,rightLL):
            insertAt = dummy  = ListNode()
            while leftLL and rightLL:
                if leftLL.val < rightLL.val:
                    insertAt.next = leftLL
                    leftLL = leftLL.next
                else:
                    insertAt.next = rightLL
                    rightLL = rightLL.next
                insertAt = insertAt.next
 
            if leftLL:
                insertAt.next = leftLL
            if rightLL:
                insertAt.next = rightLL
            return dummy.next
        def getMid(head):
            slow = head
            fast = head.next
            while fast and fast.next : 
                slow = slow.next
                fast = fast.next.next
            return slow
        
        if not head or not head.next:
            return head
        
        left = head
        right = getMid(head)
        temp = right.next 
        right.next = None
        right = temp

        leftLL = self.sortList(left)
        rightLL = self.sortList(right)
        return mergeCombine(leftLL,rightLL)
