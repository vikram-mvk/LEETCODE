'''
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    ans = ListNode(0)
    head = ans
    while l1 != None and l2 != None:
        if l1.val < l2.val:
            ans.next = ListNode(l1.val)
            l1 = l1.next
        else:
            ans.next = ListNode(l2.val)
            l2 = l2.next
        ans = ans.next

    while l1 != None:
        ans.next = ListNode(l1.val)
        ans = ans.next
        l1 = l1.next
    while l2 != None:
        ans.next = ListNode(l2.val)
        ans = ans.next
        l2 = l2.next
    return head.next
'''