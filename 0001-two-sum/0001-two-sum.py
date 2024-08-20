class Solution(object):
    def twoSum(self, nums, target):
        num_dict = {}  
        for i, num in enumerate(nums):
            res = target - num  
            if res in num_dict:  
                return [num_dict[res], i]  
            num_dict[num] = i
