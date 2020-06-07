'''
https://leetcode.com/problems/container-with-most-water/
we calculate the area at end points. we move the smaller line among the two because for max water we need two of the tallest polls

'''

def maxArea(self, height: List[int]) -> int:
    area = 0
    i = 0
    j = len(height) - 1
    while i < len(height) and j > 0:
        if height[i] > height[j]:
            this_area = height[j] * (j - i)
            j -= 1
        else:
            this_area = height[i] * (j - i)
            i += 1

        if this_area > area:
            area = this_area
    return area