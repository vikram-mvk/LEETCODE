'''

A. Kadane:
------------Idea is to compare nums[i] and nums[i] + curr_sum----------------

1. if nums[i] alone is single handedly larger than (curr_sum + nums[i] ) [indicates that then curr_sum is negative] we dont care about the curr sum anymore
and reassign curr_sum to nums[i]. (A fresh start)

2. if curr_sum+nums[i] results in a larger number than curr_sum, add it to curr_sum [indicates that then curr_sum is positive]

3. if curr_sum is greater than global max, reassing global max to curr_sum

note that We're not simply skipping any i. We're either adding nums[i] to curr_sum or
nums[i] itself becomes the curr_sum, so contiguity is maintained


'''
#Kadane's Algo
nums=[-2,1,-3,4,-1,2,1,-5,4]
i=1
curr_sum = nums[0]
global_max = nums[0]
while i < len(nums):
    curr_sum = nums[i] if nums[i]>curr_sum + nums[i] else curr_sum + nums[i]
    if global_max<curr_sum: global_max= curr_sum
    i += 1
print(global_max)