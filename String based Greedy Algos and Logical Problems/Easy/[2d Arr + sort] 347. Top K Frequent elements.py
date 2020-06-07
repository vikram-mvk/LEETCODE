'''
https://leetcode.com/problems/top-k-frequent-elements/
Concept:
1. Find the frequency of each element in  array.
2. Append the elements in res array in which indices represent frequency, i.,e lowest frequency will be at 0  and highest at len(nums)-1
3. from last index of res, add k elements from res array to another array and return it
'''

#6 line code with comments:
nums=[1,2,3,1,2]
k=3
#assign 4 variables d={}, res=[], i=len(nums)-1, arr = a 2d array of size len(nums)
d,  res,  i,  arr =   {},   [],  len(nums)-1,  [ [] for i in range(len(nums))]
for x in nums: d[x]= d[x]+ 1 if x in d else 0  #Frequency: assign 0 if it appears for the 1st time, else, add previous val + 1
for key,val in d.items(): arr[val].append(key) #array indices represent frequency. append numbers in their respective freeuency
while len(res)<k and i>=0: #start from the last index and append the elements in res, until we've appended k elements
    for x in arr[i]:
        if len(res) == k: break
        res.append(x)
    i-=1
print(res)