class Solution:
    def arraySign(self, nums) -> int:
        result = 1
        for num in nums:
            result *= num
        if result > 0:
            return 1
        elif result == 0:
            return 0
        else:
            return -1