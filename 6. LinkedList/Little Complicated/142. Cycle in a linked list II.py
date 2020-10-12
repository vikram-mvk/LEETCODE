class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head: return head
        slow=fast=head
        while fast.next and fast.next.next:
            fast=fast.next.next
            slow=slow.next
            if slow==fast: #they met at some point in the loop, but we don't know if that's the starting point of the loop
                while True: #To find the starting point,move head until it meets slow
                    if head==slow: return head
                    head=head.next
                    slow=slow.next