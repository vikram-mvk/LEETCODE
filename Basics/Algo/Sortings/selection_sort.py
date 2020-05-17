a=[5,3,7,2,6]
for i in range(len(a)):
    min=a[i]
    for j in range(i,len(a)):
        if min>a[j]:
            min=a[j]
            temp=a[i]
            a[i]=a[j] #which is the min
            a[j]=temp
print(a)