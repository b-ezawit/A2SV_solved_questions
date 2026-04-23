# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(val=0,next=head)
        ans = dummy
        while dummy:
            while dummy.next and dummy.next.val == val:
                    dummy.next = dummy.next.next
            dummy=dummy.next
        return ans.next 



