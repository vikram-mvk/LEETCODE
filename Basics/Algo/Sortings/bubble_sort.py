a=[5,3,7,2,6]
for i in range(len(a)):
    for j in range(len(a)-1):
        if(a[i]<a[j]):
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
print(a)