# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        pal = ""
        cur = head
        while cur:
            pal += str(cur.val)
            cur = cur.next

        return True if pal == pal[::-1] else False
        