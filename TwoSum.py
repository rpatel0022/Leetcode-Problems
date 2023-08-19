class Solution(object):
    def twoSum(self, nums, target):
        dictionary = {}

        for i in range(0, len(nums)):
            value = target - nums[i]
            if value in dictionary:
                return [i, dictionary[value]]
            else:
                dictionary[nums[i]] = i
        return -1

sol = Solution()
print(sol.twoSum([3, 2, 4], 6))