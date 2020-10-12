volcanic=[7000,134000,7000,14000]
non_volcanic=[7000, 134000,150000,7000]
vol={}
res=[]
for x in volcanic: vol[x] = 1 if x not in vol else vol[x]+1
for y in non_volcanic:
    if y in vol and vol[y]>0:
        res.append(y)
res.sort(reverse=True)
print(res)
