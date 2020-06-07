'''
Normal binary search but we return mid+1 if not found or return mid is found
'''
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target: return mid
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left