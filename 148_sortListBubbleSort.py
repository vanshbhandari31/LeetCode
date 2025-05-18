# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def Lcount(head):
            if head is None:
                return 0
            L=0
            temp=head
            while temp:
                L+=1
                temp=temp.next

            return L
        if head is None:
            return None
        headTemp=head
        for i in range (Lcount(head)) :
            while headTemp.next!=None:
                if(headTemp.val>headTemp.next.val):
                    temp=headTemp.val
                    headTemp.val=headTemp.next.val
                    headTemp.next.val=temp
                headTemp=headTemp.next
            headTemp=head
        return head

