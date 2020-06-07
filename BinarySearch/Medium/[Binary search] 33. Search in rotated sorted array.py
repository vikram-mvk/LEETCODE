'''
The main concept of this problem is that when we pick a middle element,
either the left segment from the middle is fully sorted or the right segment is fully sorted or both are fully sorted
example: [4,5,6,7,0,1,2] and target =0
mid = 7 . here left segment 4 5 6 is fully sorted and right segment is also fully sorted
another scenario: [2,3,4,5,6,1] and target = 3, here left is sorted but right is not.

first check if nums[mid] is the target, if yes return mid
else, we need to find a sorted segment first, to implement our binary search

if nums[middle] <= nums[right]: #if true, this indicates that the array form mid to right is sorted.
#Now we need to check if target is in this segement or not by doing -> if nums[middle] < target <= nums[right]: )
#if true, we need to search this segement alone by increasing left to mid+1 -> left = middle + 1
if not true we need to discard this segment by reducing right to mid-1 ->  (right = middle - 1)

else if nums[left]<nums[middle] holds true, left segment is sorted
#Now we are checking if target is in this segement or not -> (if nums[left] <= target < nums[middle]:)
#if yes, we need to search this segement alone by reducing right to mid-1  -> (right = middle - 1)
else:
    left = middle + 1 #if not, we need to discard this segment by increasing left to mid+1

This will make the middle element and target element equal at some point, if the target existed in the array
'''
def search(self, nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        middle = (left + right) // 2
        if nums[middle] == target: return middle
        if nums[middle] <= nums[right]: #this means that the array form mid to right is sorted.
            if nums[middle] < target <= nums[right]: #Now we are checking if target is in this segement or not
                left = middle + 1 #if yes, we need to search this segement alone by increasing left to mid+1
            else:
                right = middle - 1 #if not, we need to discard this segment by reducing right to mid-1
        else: #this means the left sub array is sorted
            if nums[left] <= target < nums[middle]: #Now we are checking if target is in this segement or not
                right = middle - 1 #if yes, we need to search this segement alone by reducing right to mid-1
            else:
                left = middle + 1 #if not, we need to discard this segment by increasing left to mid+1

    return -1