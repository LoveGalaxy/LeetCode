"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.


Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # ---------------- Solution 0 ----------- 5392ms
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    return[i, j]
        return None

        # ---------------- Solution 1 ----------- 24ms
        nums_dict = dict()
        for i in range(len(nums)):
            nums_dict[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in nums_dict and nums_dict[complement] != i:
                return [i, nums_dict[complement]]
        return None

        # ---------------- Solution 2 ----------- 24ms
        nums_dict = dict()
        for i in range(len(nums)):
            left = target - nums[i]
            if left in nums_dict:
                return [nums_dict[left], i]
            else:
                nums_dict[nums[i]] = i
        return None  

        # ---------------- Solution 3 ----------- 400ms
        # the idea of this code is identical to solution 2, but it is slower than solution 2 obviously.
        # this is becuase query value in dictionary is faster than query it in list
        for i in range(len(nums))[::-1]:
            left = target - nums[i]
            if left in nums and nums.index(left) != i:
                return [nums.index(left), i]
        return None
