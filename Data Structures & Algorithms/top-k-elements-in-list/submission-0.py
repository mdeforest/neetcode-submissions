class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        minValue = min(nums) # O(n), O(1)
        maxValue = max(nums) # O(n), O(1)
        frequencies = [0] * (maxValue - minValue + 1) 

        for item in nums:
            frequencies[item - minValue] += 1

        topK = []
        print(frequencies)
        for i in range(k):
            maxFrequency = max(frequencies)
            maxIndex = frequencies.index(maxFrequency)
            topK.append(maxIndex + minValue)
            frequencies[maxIndex] = 0

        return topK