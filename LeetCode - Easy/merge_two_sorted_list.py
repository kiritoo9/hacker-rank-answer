# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def _convert_list(data_list):
            l = []
            curr = data_list

            while curr:
                l.append(curr.val)
                curr = curr.next

            return l

        list1 = _convert_list(list1)
        list2 = _convert_list(list2)
        sorted_list = sorted(list1 + list2)

        # convert to list node
        def _convert_node(data_list):
            dummy = ListNode()
            curr = dummy

            for d in data_list:
                curr.next = ListNode(d)
                curr = curr.next

            return dummy.next

        return _convert_node(sorted_list)