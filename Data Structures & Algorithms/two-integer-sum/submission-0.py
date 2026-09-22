class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashDict = {}
        for i in range(len(nums)):
            complement = target - nums[i] #4

            if complement in hashDict:
                return [hashDict[complement], i]

            hashDict[nums[i]] = i
