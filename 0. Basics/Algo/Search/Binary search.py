#best case 0(1)... worst case o(log n)
def bin(a,l,r,k):
 if r>=l:
    mid = (l+r)//2
    if a[mid] == k:
        print("found at index",mid)
    elif a[mid]>k:
        r = mid -1
        bin(a,l,r,k)
    elif a[mid]<k:
        l=mid+1
        bin(a,l,r,k)
 else:
        print("not found")

if __name__ =="__main__":
    a = [0, 1, 2, 3, 4, 5]
    l = 0
    r = len(a) - 1
    bin(a, l, r, 6)

'''
	

'''




