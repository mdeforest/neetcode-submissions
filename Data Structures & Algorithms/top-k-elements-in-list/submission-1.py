class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        minValue = min(nums)    # O(n), O(1)
        maxValue = max(nums)    # O(n), O(1)
        frequencies = [0] * (maxValue - minValue + 1)   # O(n), O(n)

        for item in nums:   # O(1), O(1)
            frequencies[item - minValue] += 1   # O(1), O(1) 

        topK = []   # O(1), O(1)
        for i in range(k):  # O(1), O(1)
            maxFrequency = max(frequencies) # m = range of integers < n, O(m), O(1)
            maxIndex = frequencies.index(maxFrequency)  # O(n), O(1)
            topK.append(maxIndex + minValue)    # O(1), O(1)
            frequencies[maxIndex] = 0   # O(1), O(1)

        return topK