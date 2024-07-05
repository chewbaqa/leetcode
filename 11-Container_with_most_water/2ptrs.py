class Solution:
    def maxArea(self, height: List[int]) -> int:
        bestContainer = 0
        p1 = 0
        p2 = len(height) - 1

        while p1 < p2:

            w = p2 - p1
            h = min(height[p1], height[p2])
            area = w * h

            bestContainer = max(area, bestContainer)

            if height[p1] < height[p2]:
                p1 += 1
            else:
                p2 -= 1

        return bestContainer
