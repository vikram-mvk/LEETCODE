'''
def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    all = []
    for l in lists:
        while l:
            all.append(l.val)
            l = l.next

    all.sort()
    head = ListNode(0)
    temp = head
    for x in all:
        head.next = ListNode(x)
        head = head.next

    return temp.next
'''