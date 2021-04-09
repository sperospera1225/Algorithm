class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        temp = 0
        count = 0
        sum_list = list()
        for i in range(len(nums)):
            if temp < nums[i]:
                temp = nums[i]
                count += 1
                if i == len(nums) - 1:
                    summ2 = 0
                    for j in range(i - count + 1, i + 1):
                        summ2 = summ2 + nums[j]
                    sum_list.append(summ2)

            else:
                summ = 0
                for j in range(i - count, i):
                    summ += nums[j]
                temp = nums[i]
                count = 1
                sum_list.append(summ)
                if i == len(nums) - 1:
                    sum_list.append(nums[i])
                    break
        return max(sum_list)

