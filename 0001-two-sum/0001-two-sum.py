class Solution(object):
    def twoSum(self, nums, target):
        num_dict = {}
        for i, num in enumerate(nums):
            n = target - num
            if n in num_dict: 
                return [num_dict[n], i]  
            num_dict[num] = i