'''
https://leetcode.com/problems/jump-game/
Both are actually greedy approaches

Valley finding:
1.Have a variable reachable, that will store the highest index that can be reached at any given point in the loop
2.we start with i=0 and reachable = 0
3.The largest i+nums[i] value that we know so far is the reachable.
4.This value must always be greater than i. Because if its not, It means that we've encountered zero somewhere. any_index+ its_value = any_index only when its_value is zero. If the reachable is stuck at that point, i will become greater than reachable at some point in the future. At the moment, we know we can't reach the last index, so return False
5.If the loop is done, then i was always behind rechable and loop is done only when i == nums[last_index] so we can go to last_index or even more than last_index depending on the value of reachable.

Back Tracking:
1. place i at the last_index-1 th position
2. if i+nums[i] is greater than or equal to last_index it means that we can
reach the last index from that point. so now we need to check if we can reach that
point from some other point behind it. so make that point as last index
3. finally when last_index is 0, return true
'''

#Best solution
#Valley finding approach Tech Dose
def canJump(nums) -> bool:
    reachable=i=0
    while i<len(nums):
        if i>reachable: return False
        if i+nums[i]>reachable: reachable=i+nums[i]
        i+=1
    return True


#Back Tracking solution (Nick White)
def canJump(nums) -> bool:
    last_index = len(nums) - 1
    i = last_index - 1
    while i >= 0:
        if i + nums[i] >= last_index:   last_index = i
        i -= 1

    return last_index == 0
