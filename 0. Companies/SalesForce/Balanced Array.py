arr=[1,2,3,4,6]

left=[0]
for i in range(1,len(arr)): left.append(left[i-1]+arr[i-1])
right=[0]*len(arr)

for i in range(len(arr)-2,-1,-1):
    right[i]=right[i+1]+arr[i+1]

min_val=float('inf')
min_index=0
for i in range(0,len(arr)):
    if left[i]==right[i] and min_val>arr[i]: min_val,min_index=arr[i],i


print(min_val,min_index)

