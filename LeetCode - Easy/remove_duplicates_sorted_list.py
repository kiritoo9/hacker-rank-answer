# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        seen = set()
        dummy = ListNode()
        curr_b = dummy

        while head:
            if head.val not in seen:
                seen.add(head.val)
                curr_b.next = ListNode(head.val)
                curr_b = curr_b.next

            head = head.next

        return dummy.next