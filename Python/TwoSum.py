class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dictionary = {} 
        for index, value in enumerate(nums):
            difference = target - value
            if difference in dictionary:
                return [index, dictionary[difference]]
            else:
                dictionary[value] = index
