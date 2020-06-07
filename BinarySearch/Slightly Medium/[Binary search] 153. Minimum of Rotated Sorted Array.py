'''
When a sorted array is rotated nums[0] will be greater than nums[len].
therefore nums[left] will be greater than nums[right]
while this condition holds:
1. find the mid point of the array
2. If the element at the mid point is larger or equal, we haven't yet reached the original starting point of the original unrotated array
3. So we need to move further left. So Assign left to middle+1
4. if element at mid point is smaller than nums[left] we are either in the start of the array or somewhere after start, so we need to modify right to middle

'''
def findMin(self, nums: List[int]) -> int:
    left, right = 0, len(nums) - 1
    while nums[left] > nums[right]:  # if this is true, rotation exists, until the rotation exists do:
        middle = (left + right) // 2
        if nums[middle] >= nums[left]:   left = middle + 1
        else: right=  middle
    return nums[left]

'''
Tracing [3,4,5,1,2]
initially left = 3 right = 2
while 3>2 (True) mid is 5. 5 is still greater than 3. So we need to move our left to the element after 5
left=1 right=2 now while condition fails. return nums[left] will have 
'''
