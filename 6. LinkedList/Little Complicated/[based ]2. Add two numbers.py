'''
https://leetcode.com/problems/add-two-numbers/

put the numbers in correct order by using math
if reverse num is 321, correct num is (3*1)+(2*10)+(1*100) = 123
add them


'''
'''
    i=1
    j=1
    num1=0
    num2=0
   #corner case where one value is zero we just return the other linkedlist
    if l1.val==0 and l1.next==None:
        return l2
    if l2.val==0 and l2.next==None:
        return l1
    
    while(l1!=None):
        num1=(l1.val*i)+num1
        l1=l1.next
        i=i*10
    while(l2!=None):
        num2=(l2.val*j)+num2
        l2=l2.next
        j=j*10
    
    sum=num1+num2

    temp=ListNode(sum%10)
    node=temp
    sum=sum//10
    while(sum>0):
        temp.next=ListNode(sum%10)
        sum=sum//10
        temp=temp.next
    temp.next=None
    return node
    
'''