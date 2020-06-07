a=[5,3,7,2,6]
for i in range(1,len(a)):
    ptr=i
    min=a[i]
    while ptr>0 and a[ptr-1]>min:
        a[ptr]=a[ptr-1] #when a previous element is larger, we know that it should be in the current place, not in the previous place.
        ptr=ptr-1
    a[ptr]=min
print(a)
