'''
Approach 1:
One of the easiest approach where we sort the array and put the array elts
in a dict with key:value as number:last_index.
Now we loop from i=0 j=i+1.. add nums[i] and nums[j] and find the compliment of this sum in the rest of the array.
This makes it like 2sum. adding to numbers to make it a single number and then check for its compliment

Approach 2:
sort the array and loop the array form 0 to last-2
for each ith element find two numbers such that (search from i+1 to len(nums)) they add upto be a compliment of this number
if true, append the triplet and get a new unique left and right by looping or using dict
elif the triplet sum is lesser than the required sum, we need to increase the left pointer alone
ellif if its greater we need to reduce the right pointer alone
'''
def sum(nums):
    nums.sort()
    ans,d = set(),{}
    for i, x in enumerate(nums):  d[x] = i

    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            required = -(nums[i] + nums[j])
            if required in d and d[required] > j: ans.add((nums[i], nums[j], required))
    return list(ans)

class Solution:
    def threeSum(self, nums) :
        #[-1, 0, 1, 2, -1, -4]
        res = []
        nums.sort()
        #sorted [-4,-1,-1 0, 1, 2]
        last,first={},{}
        for i,x in enumerate(nums):
            last[x]=i
            if x not in first: first[x]=i
        length = len(nums)
        for i in first.values():
            if nums[i]>0: break  #When the number is positive, cant find a negative compliment after that, so break
            l, r = i+1, length-1
            required_sum = -nums[i]
            while l<r:
                current_sum = nums[l]+nums[r]
                if current_sum < required_sum: l+=1 #or  l=last[nums[l]] + 1
                elif current_sum > required_sum: r-=1 #or r = first[nums[r]] -1
                else:
                    res.append([-required_sum,nums[l],nums[r]])
                    l=last[nums[l]]+1 #if the same number is repeated, go to the last occourence of it+1 to get a unique number either Loop or using Dict
                    r=first[nums[r]]-1 #if the same number is repeated, to to the first occourence of it -1 to get a unique number either Loop or using Dict
        return res
