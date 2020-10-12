


arr=[4,3,1,2]
ref_arr=sorted(arr)
d={item:index for index,item in enumerate(arr)}
#original array's items as keys and index as values
swaps=0
for index,item in enumerate(arr):
    print(arr)
    if item!=ref_arr[index]:
        #put the correct item in this index
        arr[index]=ref_arr[index]
        print("swap1", arr)
        #put the wrong item(current one) to where correct item was in the original array
        arr[d[ref_arr[index]]] = item
        print("swap2", arr)
        #update dict to say that we've swapped one item to its correct position
        #wrong item belongs to where the correct item was
        d[item]=d[ref_arr[index]]
        #now correct item belongs to index
        d[ref_arr[index]]=index
        swaps+=1

print(swaps)
'''
arr=[7, 1, 3, 2, 4, 5, 6]
def recur(arr,swaps):
    print(arr)
    start=0
    end=len(arr)-1
    if len(arr)>=2:
        mini=arr.index(min(arr))
        if mini!=0:
            swaps+=1
            arr=swap(arr,0,mini)
        print("swapped min",arr)
        maxi = arr.index(max(arr))
        if maxi!=len(arr)-1:
            swaps+=1
            arr=swap(arr,len(arr)-1,maxi)
        print("swapped max", arr)
        start+=1
        end-=1
        return recur(arr[start:end+1],swaps)
    else:
        return swaps
def swap(arr,a,b):
    temp=arr[a]
    arr[a]=arr[b]
    arr[b]=temp
    return arr

a=recur(arr,0)
print(a)

'''