# # 1848. Minimum Distance to the Target Element
# https://leetcode.com/contest/weekly-contest-239/problems/minimum-distance-to-the-target-element/

class Solution:
    def getMinDistance(self, nums, target, start) -> int:
        idx=[]
        for i, num in enumerate(nums):
            if num==target:
                idx.append(abs(i-start))
        return min(idx)
s = Solution()
s.getMinDistance([1,2,3,4,5],5,3)