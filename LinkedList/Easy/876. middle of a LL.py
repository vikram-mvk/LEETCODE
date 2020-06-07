'''
def middleNode(self, head: ListNode) -> ListNode:
    fast = slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
'''