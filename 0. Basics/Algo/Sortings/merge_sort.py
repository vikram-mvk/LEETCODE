a=[5,3,7,2,6]

def merge(a,l,r):
    i=j=k=0
    while i<len(l) and j<len(r):
        if(l[i]<r[j]):
            a[k]=l[i]
            i+=1
        else:
            a[k]=r[j]
            j+=1
        k+=1
    while i<len(l):
        a[k]=l[i]
        i+=1
        k+=1
    while j < len(r):
        a[k] = r[j]
        j += 1
        k+=1



def merge_sort(a, n):
    if n<2:
        return
    mid=n//2
    l=[]
    r=[]
    for i in range(mid):
        l.append(a[i])
    for i in range(mid,n):
        r.append(a[i])
    merge_sort(l, len(l))
    merge_sort(r, len(r))
    merge(a,l,r)

merge_sort(a,len(a))
print(a)



