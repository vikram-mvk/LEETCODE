class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points: return 0

        points.sort(key=lambda x: x[0])

        # there is atleast one balloon, so initialize to 1
        shoot = 1
        # we're shooting each balloon at its right most border, so that there is a better chance of another baloon to overlap
        shooting_point = points[0][1]

        i = 1
        while i < len(points):
            if shooting_point >= points[i][
                0]:  # if left border of second balloon overlaps, shoot at the min of the two right borders so that both are shot.
                shooting_point = min(shooting_point, points[i][1])
            else:
                shooting_point = points[i][1]
                shoot += 1
            i += 1
        return shoot