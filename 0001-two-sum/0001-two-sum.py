class Solution(object):
    def twoSum(self, nums, target):
        memo = {}
        for i, num in enumerate(nums):
            n = target - num
            if n in memo:
                return [memo[n], i]
            memo[num] = i