class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
def build_linked_list(nums):
    dummy = ListNode()
    current = dummy

    for num in nums:
        current.next = ListNode(num)
        current = current.next

    return dummy.next