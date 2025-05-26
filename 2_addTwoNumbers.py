# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def Lreverse(l):
            curr=l
            prev=None
            while(curr):
                next=curr.next
                curr.next=prev
                prev=curr
                curr=next
            return prev

        l1new=Lreverse(l1)
        l2new=Lreverse(l2)

        l1num=""
        while(l1new):
            l1num=l1num+str(l1new.val)
            l1new=l1new.next

        l2num = ""
        while (l2new):
            l2num = l2num + str(l2new.val)
            l2new = l2new.next
        l1num=int(l1num)
        l2num=int(l2num)
        lres=l1num+l2num

        lres=str(lres)
        dummy = ListNode(0)
        current = dummy
        for ch in lres:
            current.next = ListNode(int(ch))
            current = current.next
        ans=Lreverse(dummy.next)
        return ans


