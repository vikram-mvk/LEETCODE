'''
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
Remove Duplicates in place with no extra memory

We need to use two pointers, one for tracking the place where element is to be inserted
and other for traversing the array
Tracing:
j=0 i=0 they're same. i++ . now i=1 and again 0==0. so i++
now j=0 i=2 and value of nums[2] is 1. so nums[j+1] = nums[i] => nums[1]=nums[2]. so nums[1] is now 1
array will be [0,1,1,1,2,2,3,3,4]

the same goes on until first j elements are unique
'''
nums=[0,0,1,1,1,2,2,3,3,4]
i = 1
j = 0
while i < len(nums):
    if nums[j] != nums[i]:
        j += 1
        nums[j] = nums[i]
    i += 1
print(nums[0: j + 1])