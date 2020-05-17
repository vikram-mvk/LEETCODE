'''
pre=None
        curr=head
        nxt=None
        while(curr!=None):
            nxt=curr.next
            curr.next=pre
            pre=curr
            curr=nxt
        return pre
'''