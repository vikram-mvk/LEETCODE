used=[1,2,3]
total=[3,3,3]
total.sort(reverse=True)
total_used=sum(used)
min=0
i=0
while total_used>0:
    curr=total[i]
    total_used-=curr
    if total_used>0:
        min+=1
        i+=1
        continue
    min+=1
print(min)


