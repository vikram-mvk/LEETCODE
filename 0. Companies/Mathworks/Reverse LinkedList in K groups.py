def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
    # Check the current linked list size and verify if it can be reversed
    size = 0
    temp = head
    while temp:
        size += 1
        temp = temp.next
    if k <= 1 or size < k:  return head
    # Reverse the LinkedList as usual until K
    pre, cur = None, head
    for _ in range(k):
        nxt = cur.next
        cur.next = pre
        pre = cur
        cur = nxt
    head.next = self.reverseKGroup(cur, k)
    return pre
