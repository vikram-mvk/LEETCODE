'''
Two points merge when the right boundary of one exceeds the left boundary of the other
when they merge, the updated left boundary is min of the two left boundaries and the updated right boundary is the max of the two right boundaries
'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return []

        # sort the intervals by left boundary
        intervals.sort(key=lambda x: x[0])

        i = 1
        j = 0
        while i < len(intervals):
            if intervals[j][1] >= intervals[i][0]:  # it merges, so update one of the boundary and delete the other(thus we're merging). lets update j
                intervals[j][0] = min(intervals[j][0], intervals[i][0])
                intervals[j][1] = max(intervals[j][1], intervals[i][1])
                del intervals[i]#here when you delete i the current i+1 th element takes ith position. Swapping each element is costly. So use a new array. (soln 2)
            else:
                j += 1
                i += 1
        return intervals


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return []

        # sort the intervals by left boundary
        intervals.sort(key=lambda x: x[0])
        boundaries=[intervals[0]]
        i = 1
        j = 0
        while i < len(intervals):
            if boundaries[j][1] >= intervals[i][0]:  # it merges, so update one of the boundary and delete the other(thus we're merging). lets update j
                boundaries[j][0] = min(boundaries[j][0], intervals[i][0])
                boundaries[j][1] = max(boundaries[j][1], intervals[i][1])
            else:
                boundaries.append(intervals[i])
                j += 1
            i += 1
        return boundaries
