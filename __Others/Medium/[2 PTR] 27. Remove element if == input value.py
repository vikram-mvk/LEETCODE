'''
https://leetcode.com/problems/remove-element/
Logic:
initially i=0 and j=last_index
Start from the j=0 and check if it is equal to val.
if true, replace the element with nums[i]... nums[j]=nums[i]..
i-=1
check again, if still same, replace with current i..
if not same, increment j

Run the code to visualize
'''

nums=[0,1,2,2,3,0,4,2]
val=2
i = len(nums) - 1
j = 0

while j < len(nums) and i >= j:
    print("j =",j,"i=",i,"nums[j]=",nums[j],"nums[i]=", nums[i])
    if nums[j] == val:
        print("equal to val. so replace with",i ,"th element and i-1",i-1)
        nums[j] = nums[i]
        i -= 1
    else:
        print("not equal to val. so need not be removed. do j+1 ",j+1)
        j += 1

print(nums[:j])