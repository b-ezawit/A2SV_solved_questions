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
                if leftLL.val < rightLL.val:#left smol thn right so appp left
                    insertAt.next = leftLL
                    leftLL = leftLL.next
                else:
                    insertAt.next = rightLL
                    rightLL = rightLL.next
                insertAt = insertAt.next
            # ye pura chalgea agar len same hogi toh ye sahi h but if koi node reh jayuega so need to handle that now
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
            return slow#return the mid node of the LL
        
        if not head or not head.next:
            return head
        #mtlb keval single elem list hai whic means already sorted h
        
        left = head
        right = getMid(head)
        temp = right.next#this holds the right arr first node 
        right.next = None#mtlb left arr ka last node ko nul kr diya
        right = temp

        leftLL = self.sortList(left)
        rightLL = self.sortList(right)
        return mergeCombine(leftLL,rightLL)
