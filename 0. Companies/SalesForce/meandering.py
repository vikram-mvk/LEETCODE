arr=[5,2,7,8,-2,25,25]
arr.sort()
res=[]
i=0
j=len(arr)-1
while i<j:
    res.append(arr[j])
    res.append(arr[i])
    i+=1
    j-=1
if len(arr)%2!=0: res.append(arr[i])
print(res)


