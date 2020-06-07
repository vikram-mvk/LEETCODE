#slightly medium because we need to use binary search

a=100
def bruteforce(a):
    i=0
    while i*i<a:
        i+=1
    return i
    #Time complecity O(root(N))

ans=bruteforce(a)
if ans*ans==a:
    print(ans)
else:
    print("not a perfect square")

'''
def binarysearch(a,start,end,arr):
    mid=start+end//2


    return mid

arr=[]
x=a//2

for i in range(1,end):
    arr.append(i)
binarysearch(a,0,end,arr)
'''