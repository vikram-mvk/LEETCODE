class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        pos = 0
        '''
        The idea is to just take non zero elements and insert to pos.
        Pos would have gone only as far as the number of non zero elements in the array. 
        so after the first iteration, until pos<len(nums), nums[pos]=0
        '''
        while i < len(nums):
            if nums[i] != 0:
                nums[pos] = nums[i]
                pos += 1
            i += 1

        while pos < len(nums):
            nums[pos] = 0
            pos += 1



