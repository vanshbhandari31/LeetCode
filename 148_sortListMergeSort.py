# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from encodings import normalize_encoding


class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        def getmid(head):
            slow,fast=head,head.next
            while fast and fast.next:
                slow=slow.next
                fast=fast.next.next
            mid=slow.next
            slow.next=None
            return mid
        def merge(l1,l2):
            dummy=ListNode()
            tail=dummy
            while l1 and l2:
                if l1.val<l2.val:
                    tail.next=l1
                    l1= l1.next
                else:
                    tail.next=l2
                    l2=l2.next
                tail=tail.next
            tail.next=l1 if l1 else l2
            return dummy.next
        mid=getmid(head)
        left=self.sortList(head)
        right=self.sortList(mid)
        return merge(left,right)
