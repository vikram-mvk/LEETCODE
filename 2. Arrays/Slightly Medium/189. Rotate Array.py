'''
1. Brute Force: shifting elements one by one
2. Reverse:
example: [1,2,3,4,5]  k=2 ans=[4,5,1,2,3]
Reverse the whole array [5,4,3,2,1]
Reverse first k elts: [4,5,3,2,1]
Reverse Array from k to n: [4,5,1,2,3] -> ans

3. Cyclic Replacement:
example: [1,2,3,4,5]  k=2 ans=[5,4,1,2,3]

'''

#soln 2
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def rev(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        k = k % len(nums)
        # reverse the whole array
        rev(0, len(nums) - 1)
        rev(0, k - 1)
        rev(k, len(nums) - 1)
#soln 3
def rotate(self, nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    k %= n

    start = count = 0
    while count < n:
        curr_index, curr_val = start, nums[start]
        while True:
            next_index = (curr_index + k) % n
            nums[next_index], curr_val = curr_val, nums[next_index]
            curr_index = next_index
            count += 1

            if start == curr_index:
                break
        start += 1