class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numZeros = 0
        product =  1

        for item in nums:
            if item == 0:
                numZeros += 1
            else:
                product *= item

        output = []

        for i in range(len(nums)):
            if nums[i] == 0 and numZeros >= len(nums) - 1 and len(nums) > 2:
                output.append(0)
            elif nums[i] == 0 and numZeros > 1:
                output.append(0)
            elif nums[i] == 0:
                output.append(product)
            elif numZeros > 0:
                output.append(0)
            else:
                output.append(product * 1 // nums[i] )

        return output
